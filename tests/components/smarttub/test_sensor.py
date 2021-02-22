"""Test the SmartTub sensor platform."""

from . import trigger_update


async def test_sensors(spa, setup_entry, hass):
    """Test the sensors."""

    entity_id = f"sensor.{spa.brand}_{spa.model}_state"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "normal"

    spa.get_status.return_value.state = "BAD"
    await trigger_update(hass)
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "bad"

    entity_id = f"sensor.{spa.brand}_{spa.model}_flow_switch"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "open"

    entity_id = f"sensor.{spa.brand}_{spa.model}_ozone"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "off"

    entity_id = f"sensor.{spa.brand}_{spa.model}_uv"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "off"

    entity_id = f"sensor.{spa.brand}_{spa.model}_blowout_cycle"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "inactive"

    entity_id = f"sensor.{spa.brand}_{spa.model}_cleanup_cycle"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "inactive"

    entity_id = f"sensor.{spa.brand}_{spa.model}_primary_filtration_cycle"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "inactive"
    assert state.attributes["duration"] == 4
    assert state.attributes["last_updated"] is not None
    assert state.attributes["mode"] == "normal"
    assert state.attributes["start_hour"] == 2

    entity_id = f"sensor.{spa.brand}_{spa.model}_secondary_filtration_cycle"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "inactive"
    assert state.attributes["last_updated"] is not None
    assert state.attributes["mode"] == "away"
