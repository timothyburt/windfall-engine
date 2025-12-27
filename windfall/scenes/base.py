import json
import os
from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self, core):
        self.core = core
        self.version = self._load_version()

    def _load_version(self):
        """Helper to pull versioning from the updates folder."""
        # Adjust path if you run from root or engine folder
        path = os.path.join("updates", "version.json")
        try:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    data = json.load(f)
                    return data.get("version", "0.0.0")
        except Exception:
            pass
        return "0.0.0"

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, renderer):
        pass

    @abstractmethod
    def handle_input(self, event):
        pass