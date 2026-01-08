"""DataUpdateCoordinator for Komfovent."""

import logging
from datetime import timedelta
from typing import Any

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_PROTOCOL
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.typing import UNDEFINED, UndefinedType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from pymodbus.exceptions import ModbusException

from . import registers
from .const import (
    Protocol,
    CONF_PROTOCOL,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    ConnectedPanels,
    Controller,
)
from .helpers import get_version_from_int

_LOGGER = logging.getLogger(__name__)

FUNC_VER_AQ_HUMIDITY = 38
FUNC_VER_EXHAUST_TEMP = 67


class KomfoventCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Komfovent data."""

    controller: Controller = Controller.NA
    func_version: int = 0

    def __init__(
        self,
        hass: HomeAssistant,
        *,
        config_entry: config_entries.ConfigEntry | None | UndefinedType = UNDEFINED,
        **kwargs: Any,
    ) -> None:
        """Initialize."""
        from .modbus import KomfoventModbusClient  # NOQA: PLC0415 (easier to mock)

        kwargs.setdefault("name", DOMAIN)
        kwargs.setdefault("update_interval", timedelta(seconds=DEFAULT_SCAN_INTERVAL))

        super().__init__(hass, _LOGGER, config_entry=config_entry, **kwargs)

        self.client = KomfoventModbusClient(
            host=config_entry.data[CONF_HOST],
            port=config_entry.data[CONF_PORT],
            protocol=config_entry.data[CONF_PROTOCOL] or Protocol.AUTO,
        )

    async def connect(self) -> bool:
        """Connect to the Modbus device."""
        connected = await self.client.connect()

        connection_error = "Failed to connect to Komfovent device"
        if not connected:
            raise ConfigEntryNotReady(connection_error)

        # The C4 Controller (PING2) doesn't have any version information or
        # any other identifiable information. You have to know upfront that
        # you're communicating with a C4 unit.
        if self.client.protocol == Protocol.C4:
            self.controller = Controller.C4
            self.func_version = 0
            return True
        
        error_msg = "Failed to read controller firmware version"
        try:
            # Get firmware version and extract functional version from it
            fw_data = await self.client.read(registers.C6.REG_FIRMWARE)
            fw_version = get_version_from_int(fw_data)
            self.controller = fw_version[0]
            self.func_version = fw_version[4]
        except (ConnectionError, ModbusException) as error:
            _LOGGER.warning("%s: %s", error_msg, error)
            raise ConfigEntryNotReady(error_msg) from error

        return True

    async def _async_update_data_C4(self) -> dict[str, Any]:
        """Fetch data from Komfovent."""

        data = {}

        for register in registers.C4.POWER.sublist(13):
            data.update({register: await self.client.read(register)})

        for register in registers.C4.VENTILATION_LEVEL_MANUAL.sublist(2):
            data.update({register: await self.client.read(register)})

        for register in registers.C4.MODE.sublist(1):
            data.update({register: await self.client.read(register)})

        return data

    async def _async_update_data_C6(self) -> dict[str, Any]:
        """Fetch data from Komfovent."""

        data = {}

        # Read primary control (1-34)
        regs = registers.C6.REG_POWER.sublist(34)
        
        # Read connectivity, extra control (35-44)
        # This has not been tested yet, it may be implemented in the future

        # Read modes (100-158)
        regs += registers.C6.REG_AWAY_FAN_SUPPLY.sublist(59)
            
        # Read humidity setpoints (159-162)
        # This has not been tested yet, it may be implemented in the future

        # Read Eco and air quality (200-217)
        if (
            self.controller in {Controller.C6, Controller.C6M}
            and self.func_version < FUNC_VER_AQ_HUMIDITY
        ):
            regs += registers.C6.REG_ECO_MIN_TEMP.sublist(15)
        else:
            regs += registers.C6.REG_ECO_MIN_TEMP.sublist(18)

        # Skip scheduler (300-555)

        # Read active alarms (600-610)
        regs += registers.C6.REG_ACTIVE_ALARMS_COUNT.sublist(11)
            
        # Skip alarm history (611-861)

        # Read monitoring (900-957)
        if (
            self.controller in {Controller.C6, Controller.C6M}
            and self.func_version < FUNC_VER_AQ_HUMIDITY
        ):
            regs += registers.C6.REG_STATUS.sublist(56)
        else:
            regs += registers.C6.REG_STATUS.sublist(58)
        
        # Read digital outputs (958-960)
        # This has not been tested yet, it may be implemented in the future

        for register in regs:
            data.update({register: await self.client.read(register)})

        # Read exhaust temperature (961)
        if (
            self.controller in {Controller.C6, Controller.C6M}
            and self.func_version >= FUNC_VER_EXHAUST_TEMP
        ):
            try:
                data.update({registers.C6.REG_EXHAUST_TEMP: await self.client.read(registers.C6.REG_EXHAUST_TEMP)})
            except (ConnectionError, ModbusException) as error:
                _LOGGER.debug("Failed to read exhaust temperature: %s", error)

        # Read controller firmware version (1000-1001)
        try:
            data.update({registers.C6.REG_FIRMWARE: await self.client.read(registers.C6.REG_FIRMWARE)})
        except (ConnectionError, ModbusException) as error:
            _LOGGER.warning("Failed to read controller firmware version: %s", error)

        # Read panel 1 firmware version (1002-1003)
        if data.get(registers.C6.REG_CONNECTED_PANELS, 0) in [
            ConnectedPanels.PANEL1,
            ConnectedPanels.BOTH,
        ]:
            try:
                data.update({registers.C6.REG_PANEL1_FW: await self.client.read(registers.C6.REG_PANEL1_FW)})
            except (ConnectionError, ModbusException) as error:
                _LOGGER.warning(
                    "Failed to read panel 1 firmware version: %s", error
                )

        # Read panel 2 firmware version (1004-1005)
        if data.get(registers.C6.REG_CONNECTED_PANELS, 0) in [
            ConnectedPanels.PANEL2,
            ConnectedPanels.BOTH,
        ]:
            try:
                data.update({registers.C6.REG_PANEL2_FW: await self.client.read(registers.C6.REG_PANEL2_FW)})
            except (ConnectionError, ModbusException) as error:
                _LOGGER.warning(
                    "Failed to read panel 2 firmware version: %s", error
                )
                
        return data

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from Komfovent."""

        data = {}

        try:
            if self.controller == Controller.C4:
                data = await self._async_update_data_C4()
            else:
                data = await self._async_update_data_C6()

        except (ConnectionError, ModbusException) as error:
            _LOGGER.warning("Error communicating with Komfovent: %s", error)
            raise UpdateFailed from error

        return data
