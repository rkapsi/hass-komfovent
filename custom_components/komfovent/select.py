"""Select platform for Komfovent."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from enum import IntEnum

from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import registers, services
from .const import (
    DOMAIN,
    AirQualitySensorType,
    CoilType,
    Controller,
    ControlStage,
    FlowControl,
    HeatRecoveryControl,
    MicroVentilation,
    OperationMode,
    OutdoorHumiditySensor,
    OverrideActivation,
    SchedulerMode,
    TemperatureControl,
    Season,
)

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import KomfoventCoordinator

_LOGGER = logging.getLogger(__name__)


def _create_selectors_C4(coordinator: KomfoventCoordinator) -> list[KomfoventSelect]:
    return [
        KomfoventOperationModeSelect(
            coordinator=coordinator,
            register=registers.C4.SEASON,
            enum_class=Season,
            entity_description=SelectEntityDescription(
                key="season",
                name="Season",
                translation_key="season",
                options=[season.name.lower() for season in Season],
            ),
        ),
    ]

def _create_selectors_C6(coordinator: KomfoventCoordinator) -> list[KomfoventSelect]:
    entities = [
        KomfoventOperationModeSelect(
            coordinator=coordinator,
            register=registers.C6.REG_OPERATION_MODE,
            enum_class=OperationMode,
            entity_description=SelectEntityDescription(
                key="operation_mode",
                name="Operation mode",
                translation_key="operation_mode",
                options=[mode.name.lower() for mode in OperationMode],
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_SCHEDULER_MODE,
            enum_class=SchedulerMode,
            entity_description=SelectEntityDescription(
                key="scheduler_mode",
                name="Scheduler mode",
                options=[mode.name.lower() for mode in SchedulerMode],
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_TEMP_CONTROL,
            enum_class=TemperatureControl,
            entity_description=SelectEntityDescription(
                key="temperature_control",
                name="Temperature control",
                entity_category=EntityCategory.CONFIG,
                options=[mode.name.lower() for mode in TemperatureControl],
                entity_registry_enabled_default=False,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_AQ_SENSOR1_TYPE,
            enum_class=AirQualitySensorType,
            entity_description=SelectEntityDescription(
                key="aq_sensor1_type",
                name="AQ Sensor 1 Type",
                entity_category=EntityCategory.CONFIG,
                options=[mode.name.lower() for mode in AirQualitySensorType],
                entity_registry_enabled_default=False,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_AQ_OUTDOOR_HUMIDITY,
            enum_class=OutdoorHumiditySensor,
            entity_description=SelectEntityDescription(
                key="aq_outdoor_humidity_sensor",
                name="AQ Outdoor Humidity Sensor",
                entity_category=EntityCategory.CONFIG,
                icon="mdi:water-percent",
                options=[mode.name.lower() for mode in OutdoorHumiditySensor],
                entity_registry_enabled_default=False,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_ECO_HEAT_RECOVERY,
            enum_class=HeatRecoveryControl,
            entity_description=SelectEntityDescription(
                key="eco_heat_recovery",
                name="ECO Heat Recovery",
                icon="mdi:heat-wave",
                options=[mode.name.lower() for mode in HeatRecoveryControl],
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_OVERRIDE_ACTIVATION,
            enum_class=OverrideActivation,
            entity_description=SelectEntityDescription(
                key="override_activation",
                name="Override Activation",
                options=[mode.name.lower() for mode in OverrideActivation],
                entity_registry_enabled_default=True,
                entity_registry_visible_default=False,
                entity_category=EntityCategory.CONFIG,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_HOLIDAYS_MICRO_VENT,
            enum_class=MicroVentilation,
            entity_description=SelectEntityDescription(
                key="holidays_micro_ventilation",
                name="Holidays Micro-ventilation",
                options=[mode.name.lower() for mode in MicroVentilation],
                entity_registry_enabled_default=True,
                entity_registry_visible_default=False,
                entity_category=EntityCategory.CONFIG,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_STAGE1,
            enum_class=ControlStage,
            entity_description=SelectEntityDescription(
                key="control_stage_1",
                name="Control Stage 1",
                options=[mode.name.lower() for mode in ControlStage],
                entity_registry_enabled_default=False,
                entity_category=EntityCategory.CONFIG,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_STAGE2,
            enum_class=ControlStage,
            entity_description=SelectEntityDescription(
                key="control_stage_2",
                name="Control Stage 2",
                options=[mode.name.lower() for mode in ControlStage],
                entity_registry_enabled_default=False,
                entity_category=EntityCategory.CONFIG,
            ),
        ),
        KomfoventSelect(
            coordinator=coordinator,
            register=registers.C6.REG_EXTERNAL_COIL_TYPE,
            enum_class=CoilType,
            entity_description=SelectEntityDescription(
                key="external_coil_type",
                name="External Coil Type",
                options=[mode.name.lower() for mode in CoilType],
                entity_registry_enabled_default=False,
                entity_category=EntityCategory.CONFIG,
            ),
        ),
    ]

    # Flow control, AQ Sensor 2 & Control Stage 3 only available on C6/C6M
    if coordinator.controller in {Controller.C6, Controller.C6M}:
        entities.extend(
            [
                KomfoventSelect(
                    coordinator=coordinator,
                    register=registers.C6.REG_FLOW_CONTROL,
                    enum_class=FlowControl,
                    entity_description=SelectEntityDescription(
                        key="flow_control",
                        name="Flow control",
                        entity_category=EntityCategory.CONFIG,
                        options=[mode.name.lower() for mode in FlowControl],
                        entity_registry_enabled_default=False,
                    ),
                ),
                KomfoventSelect(
                    coordinator=coordinator,
                    register=registers.C6.REG_AQ_SENSOR2_TYPE,
                    enum_class=AirQualitySensorType,
                    entity_description=SelectEntityDescription(
                        key="aq_sensor2_type",
                        name="AQ Sensor 2 Type",
                        entity_category=EntityCategory.CONFIG,
                        options=[mode.name.lower() for mode in AirQualitySensorType],
                        entity_registry_enabled_default=False,
                    ),
                ),
                KomfoventSelect(
                    coordinator=coordinator,
                    register=registers.C6.REG_STAGE3,
                    enum_class=ControlStage,
                    entity_description=SelectEntityDescription(
                        key="control_stage_3",
                        name="Control Stage 3",
                        options=[mode.name.lower() for mode in ControlStage],
                        entity_registry_enabled_default=False,
                        entity_category=EntityCategory.CONFIG,
                    ),
                ),
            ]
        )

        return entities

async def create_selectors(coordinator: KomfoventCoordinator) -> list[KomfoventSelect]:
    """Create a list of selector entities."""
    if coordinator.controller == Controller.C4:
        return _create_selectors_C4(coordinator)
    else:
        return _create_selectors_C6(coordinator)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Komfovent select entities."""
    coordinator: KomfoventCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    async_add_entities(await create_selectors(coordinator))


class KomfoventSelect(CoordinatorEntity, SelectEntity):
    """Representation of a Komfovent select entity."""

    _attr_has_entity_name: ClassVar[bool] = True

    def __init__(
        self,
        coordinator: KomfoventCoordinator,
        register: registers.Register,
        enum_class: type[IntEnum],
        entity_description: SelectEntityDescription,
    ) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self.register = register
        self.enum_class = enum_class
        self.entity_description = entity_description
        self._attr_unique_id = (
            f"{coordinator.config_entry.entry_id}_{entity_description.key}"
        )
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.config_entry.entry_id)},
            "name": coordinator.config_entry.title,
            "manufacturer": "Komfovent",
            "model": None,
        }

    @property
    def current_option(self) -> str | None:
        """Return the current selected option."""
        if not self.coordinator.data:
            return None

        mode = self.coordinator.data.get(self.register)
        try:
            return self.enum_class(mode).name.lower()
        except ValueError:
            return None

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        try:
            mode = self.enum_class[option.upper()]
        except ValueError:
            _LOGGER.warning("Invalid operation mode: %s", option)
            return

        await self.coordinator.client.write(self.register, mode.value)

        await self.coordinator.async_request_refresh()


class KomfoventOperationModeSelect(KomfoventSelect):
    """Special select entity for operation mode that handles power and auto mode."""

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        await services.set_operation_mode(self.coordinator, option)
