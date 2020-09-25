"""Typing Helpers for Home Assistant."""
from typing import Any, Dict, Mapping, Optional, Tuple, Union

import homeassistant.core

GPSType = Tuple[float, float]
ConfigType = Dict[str, Any]
ContextType = homeassistant.core.Context
DiscoveryInfoType = Dict[str, Any]
EventType = homeassistant.core.Event
HomeAssistantType = homeassistant.core.HomeAssistant
ServiceCallType = homeassistant.core.ServiceCall
ServiceDataType = Dict[str, Any]
StateType = Union[None, str, int, float]
TemplateVarsType = Optional[Mapping[str, Any]]

# Custom type for recorder Queries
QueryType = Any
