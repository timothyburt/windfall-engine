from collections import deque
from .events import WindfallEvent, EventType
from windfall.scenes.menu import MainMenuScene # We'll create this next

class WindfallCore:
    def __init__(self):
        self.running = True
        self.event_queue: deque[WindfallEvent] = deque()
        
        # New: The Scene Stack
        # We initialize with the MainMenuScene
        self.scene_stack = [MainMenuScene(self)]

    @property
    def active_scene(self):
        """Returns the scene currently at the top of the stack."""
        return self.scene_stack[-1] if self.scene_stack else None

    def post_event(self, event: WindfallEvent):
        self.event_queue.append(event)

    def update(self):
        while self.event_queue:
            event = self.event_queue.popleft()

            # 1. Global Engine Events (Priority)
            if event.type == EventType.QUIT:
                self.running = False
                return

            # 2. Delegate to the Active Scene
            if self.active_scene:
                self.active_scene.handle_input(event)