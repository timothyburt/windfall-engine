from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self, core):
        self.core = core

    @abstractmethod
    def handle_input(self, event):
        """Process engine events specific to this scene."""
        pass

    @abstractmethod
    def render(self, renderer):
        """Draw the scene using the provided renderer."""
        pass