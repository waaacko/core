"""The tests for Media player device triggers."""
import pytest

import homeassistant.components.automation as automation
from homeassistant.components.media_player import DOMAIN
from homeassistant.const import (
    STATE_IDLE,
    STATE_OFF,
    STATE_ON,
    STATE_PAUSED,
    STATE_PLAYING,
)
from homeassistant.helpers import device_registry
from homeassistant.setup import async_setup_component

from tests.common import (
    MockConfigEntry,
    assert_lists_same,
    async_get_device_automations,
    async_mock_service,
    mock_device_registry,
    mock_registry,
)
from tests.components.blueprint.conftest import stub_blueprint_populate  # noqa


@pytest.fixture
def device_reg(hass):
    """Return an empty, loaded, registry."""
    return mock_device_registry(hass)


@pytest.fixture
def entity_reg(hass):
    """Return an empty, loaded, registry."""
    return mock_registry(hass)


@pytest.fixture
def calls(hass):
    """Track calls to a mock service."""
    return async_mock_service(hass, "test", "automation")


async def test_get_triggers(hass, device_reg, entity_reg):
    """Test we get the expected triggers from a media player."""
    config_entry = MockConfigEntry(domain="test", data={})
    config_entry.add_to_hass(hass)
    device_entry = device_reg.async_get_or_create(
        config_entry_id=config_entry.entry_id,
        connections={(device_registry.CONNECTION_NETWORK_MAC, "12:34:56:AB:CD:EF")},
    )
    entity_reg.async_get_or_create(DOMAIN, "test", "5678", device_id=device_entry.id)

    trigger_types = {"turned_on", "turned_off", "idle", "paused", "playing"}
    expected_triggers = [
        {
            "platform": "device",
            "domain": DOMAIN,
            "type": trigger,
            "device_id": device_entry.id,
            "entity_id": f"{DOMAIN}.test_5678",
        }
        for trigger in trigger_types
    ]
    triggers = await async_get_device_automations(hass, "trigger", device_entry.id)
    assert_lists_same(triggers, expected_triggers)


async def test_if_fires_on_state_change(hass, calls):
    """Test triggers firing."""
    hass.states.async_set("media_player.entity", STATE_OFF)

    data_template = (
        "{label} - {{{{ trigger.platform}}}} - "
        "{{{{ trigger.entity_id}}}} - {{{{ trigger.from_state.state}}}} - "
        "{{{{ trigger.to_state.state}}}} - {{{{ trigger.for }}}}"
    )
    trigger_types = {"turned_on", "turned_off", "idle", "paused", "playing"}

    assert await async_setup_component(
        hass,
        automation.DOMAIN,
        {
            automation.DOMAIN: [
                {
                    "trigger": {
                        "platform": "device",
                        "domain": DOMAIN,
                        "device_id": "",
                        "entity_id": "media_player.entity",
                        "type": trigger,
                    },
                    "action": {
                        "service": "test.automation",
                        "data_template": {"some": data_template.format(label=trigger)},
                    },
                }
                for trigger in trigger_types
            ]
        },
    )

    # Fake that the entity is turning on.
    hass.states.async_set("media_player.entity", STATE_ON)
    await hass.async_block_till_done()
    assert len(calls) == 1
    assert (
        calls[0].data["some"]
        == "turned_on - device - media_player.entity - off - on - None"
    )

    # Fake that the entity is turning off.
    hass.states.async_set("media_player.entity", STATE_OFF)
    await hass.async_block_till_done()
    assert len(calls) == 2
    assert (
        calls[1].data["some"]
        == "turned_off - device - media_player.entity - on - off - None"
    )

    # Fake that the entity becomes idle.
    hass.states.async_set("media_player.entity", STATE_IDLE)
    await hass.async_block_till_done()
    assert len(calls) == 3
    assert (
        calls[2].data["some"]
        == "idle - device - media_player.entity - off - idle - None"
    )

    # Fake that the entity starts playing.
    hass.states.async_set("media_player.entity", STATE_PLAYING)
    await hass.async_block_till_done()
    assert len(calls) == 4
    assert (
        calls[3].data["some"]
        == "playing - device - media_player.entity - idle - playing - None"
    )

    # Fake that the entity is paused.
    hass.states.async_set("media_player.entity", STATE_PAUSED)
    await hass.async_block_till_done()
    assert len(calls) == 5
    assert (
        calls[4].data["some"]
        == "paused - device - media_player.entity - playing - paused - None"
    )
