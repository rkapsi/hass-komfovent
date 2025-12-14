"""Modbus communication handler for Komfovent."""

import asyncio
import logging

from pymodbus import ModbusException
from pymodbus.client import AsyncModbusTcpClient

from .const import Protocol

#from .registers import (
#    REGISTERS_16BIT_SIGNED,
#    REGISTERS_16BIT_UNSIGNED,
#    REGISTERS_32BIT_UNSIGNED,
#)

from .registers import (
    Access,
    Datatype,
    Register,
)

_LOGGER = logging.getLogger(__name__)


class KomfoventModbusClient:
    """Modbus client for Komfovent devices."""

    def __init__(self, host: str, port: int = 502, protocol = Protocol.AUTO) -> None:
        """Initialize the Modbus client."""
        self.client = AsyncModbusTcpClient(
            host=host,
            port=port,
            timeout=5,
            retries=3,
            reconnect_delay=5,
            reconnect_delay_max=60,
        )

        self.protocol = protocol
        self._lock = asyncio.Lock()

    async def connect(self) -> bool:
        """Connect to the Modbus device."""
        return await self.client.connect()

    async def close(self) -> None:
        """Close the Modbus connection."""
        self.client.close()

    async def read(self, register: Register) -> int:
        """Read holding register(s) and return value."""
        async with self._lock:
            
            result = await self.client.read_holding_registers(
                address=register.address, count=register.datatype.size
            )

        if result.isError():
            msg = f"Error reading registers at {register}"
            raise ModbusException(msg)

        if register.datatype == Datatype.binary:
            return 0 if result.registers[0] == 0 else 1
        
        elif register.datatype == Datatype.uint16:
            return result.registers[0]
        
        elif register.datatype == Datatype.int16:
            return result.registers[0] - (result.registers[0] >> 15 << 16)
        
        elif register.datatype == Datatype.uint32:
            return (result.registers[0] << 16) + result.registers[1]

        raise NotImplementedError()

    async def write(self, register: Register, value: int) -> None:
        """Write to holding register(s)."""

        if register.access == Access.READ_ONLY:
            raise ModbusException()
        
        async with self._lock:
            if register.datatype == Datatype.binary:
                # Write 0 or 1
                result = await self.client.write_register(register.address, 0 if value == 0 else 1)

            elif register.datatype == Datatype.uint16:
                # Write unsigned value as-is
                result = await self.client.write_register(register.address, value)

            elif register.datatype == Datatype.int16:
                # Convert signed value to 16-bit unsigned for Modbus
                result = await self.client.write_register(register.address, value & 0xFFFF)

            elif register.datatype == Datatype.uint32:
                # Split 32-bit value into two 16-bit values
                high_word = (value >> 16) & 0xFFFF
                low_word = value & 0xFFFF

                # Write both words in a single transaction
                result = await self.client.write_registers(
                    address=register.address, values=[high_word, low_word]
                )
            else:
                msg = (
                    f"Register {register} not found in either "
                    "16-bit or 32-bit register sets"
                )
                raise NotImplementedError(msg)
            
        if result.isError():
            msg = f"Error writing register at {register}"
            raise ModbusException(msg)
