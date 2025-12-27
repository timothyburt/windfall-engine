from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional

class EventType(Enum):
    """The vocabulary of the Windfall Engine."""
    # System Events
    QUIT = auto()
    
    # Input/Navigation Events
    MENU_UP = auto()
    MENU_DOWN = auto()
    MENU_SELECT = auto()

@dataclass
class WindfallEvent:
    """A packet of information describing what happened."""
    type: EventType
    data: Optional[Any] = None