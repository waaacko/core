"""Platform for binary sensor integration."""
import logging

from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_DOOR,
    DEVICE_CLASS_HEAT,
    DEVICE_CLASS_MOISTURE,
    DEVICE_CLASS_MOTION,
    DEVICE_CLASS_SMOKE,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType

from .const import DOMAIN
from .devolo_device import DevoloDeviceEntity

_LOGGER = logging.getLogger(__name__)

DEVICE_CLASS_MAPPING = {
    "Water alarm": DEVICE_CLASS_MOISTURE,
    "Home Security": DEVICE_CLASS_MOTION,
    "Smoke Alarm": DEVICE_CLASS_SMOKE,
    "Heat Alarm": DEVICE_CLASS_HEAT,
    "door": DEVICE_CLASS_DOOR,
}


async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigEntry, async_add_entities
) -> None:
    """Get all binary sensor and multi level sensor devices and setup them via config entry."""
    entities = []

    for device in hass.data[DOMAIN]["homecontrol"].binary_sensor_devices:
        for binary_sensor in device.binary_sensor_property:
            entities.append(
                DevoloBinaryDeviceEntity(
                    homecontrol=hass.data[DOMAIN]["homecontrol"],
                    device_instance=device,
                    element_uid=binary_sensor,
                )
            )
    for device in hass.data[DOMAIN]["homecontrol"].devices.values():
        if hasattr(device, "remote_control_property"):
            for remote in device.remote_control_property:
                for index in range(
                    1, device.remote_control_property[remote].key_count + 1
                ):
                    entities.append(
                        DevoloRemoteControl(
                            homecontrol=hass.data[DOMAIN]["homecontrol"],
                            device_instance=device,
                            element_uid=remote,
                            key=index,
                        )
                    )
    async_add_entities(entities, False)


class DevoloBinaryDeviceEntity(DevoloDeviceEntity, BinarySensorEntity):
    """Representation of a binary sensor within devolo Home Control."""

    def __init__(self, homecontrol, device_instance, element_uid):
        """Initialize a devolo binary sensor."""
        self._binary_sensor_property = device_instance.binary_sensor_property.get(
            element_uid
        )

        super().__init__(
            homecontrol=homecontrol,
            device_instance=device_instance,
            element_uid=element_uid,
        )

        self._device_class = DEVICE_CLASS_MAPPING.get(
            self._binary_sensor_property.sub_type
            or self._binary_sensor_property.sensor_type
        )

        if self._device_class is None:
            if device_instance.binary_sensor_property.get(element_uid).sub_type != "":
                self._name += f" {device_instance.binary_sensor_property.get(element_uid).sub_type}"
            else:
                self._name += f" {device_instance.binary_sensor_property.get(element_uid).sensor_type}"

        self._value = self._binary_sensor_property.state

    @property
    def is_on(self):
        """Return the state."""
        return self._value

    @property
    def device_class(self):
        """Return device class."""
        return self._device_class


class DevoloRemoteControl(DevoloDeviceEntity, BinarySensorEntity):
    """Representation of a remote control within devolo Home Control."""

    def __init__(self, homecontrol, device_instance, element_uid, key):
        """Initialize a devolo remote control."""
        self._remote_control_property = device_instance.remote_control_property.get(
            element_uid
        )

        super().__init__(
            homecontrol=homecontrol,
            device_instance=device_instance,
            element_uid=f"{element_uid}_{key}",
        )

        self._key = key
        self._state = False

    @property
    def is_on(self):
        """Return the state."""
        return self._state

    def _sync(self, message):
        """Update the binary sensor state."""
        if (
            message[0] == self._remote_control_property.element_uid
            and message[1] == self._key
        ):
            self._state = True
        elif (
            message[0] == self._remote_control_property.element_uid and message[1] == 0
        ):
            self._state = False
        elif message[0].startswith("hdm"):
            self._available = self._device_instance.is_online()
        else:
            _LOGGER.debug("No valid message received: %s", message)
        self.schedule_update_ha_state()
