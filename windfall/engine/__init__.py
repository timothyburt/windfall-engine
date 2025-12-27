# windfall/engine/__init__.py

# Import everything into the engine namespace
from .core.core import WindfallCore
from .renderers.tui import TUIRenderer
from .scenes.base import BaseScene
from .scenes.splash import SplashScene
from .scenes.menu import MainMenuScene

# This allows you to do: from windfall.engine import SplashScene
__all__ = [
    'WindfallCore',
    'TUIRenderer',
    'BaseScene',
    'SplashScene',
    'MainMenuScene'
]