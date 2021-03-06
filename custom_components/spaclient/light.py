import logging

# Import the device class from the component that you want to support
from custom_components import spaclient
from homeassistant.components.light import LightEntity
from datetime import timedelta

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = spaclient.INTERVAL


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Setup the sensor platform."""
    spa_data = spaclient.NETWORK
    async_add_entities([SpaLight(spa_data)])


class SpaLight(LightEntity):
    """Representation of a Spa light."""

    def __init__(self, data):
        """Initialize the device."""
        self._spa = data.spa

    @property
    def name(self):
        """Return the name of the device."""
        return 'Spa Light'

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._spa.get_light()

    async def async_turn_on(self, **kwargs):
        """Instruct the light to turn on."""
        _LOGGER.info("Turning on Spa Light")
        self._spa.set_light(True)
        _LOGGER.info("Spa Light status %s", self._spa.get_light())

    async def async_turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        _LOGGER.info("Turning off Spa Light")
        self._spa.set_light(False)
        _LOGGER.info("Spa Light status %s", self._spa.get_light())

    async def async_update(self):
        """Fetch new state data for the sensor."""
        self._spa.read_all_msg()
