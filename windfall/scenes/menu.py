from windfall.scenes.base import BaseScene
from windfall.core import EventType

class MainMenuScene(BaseScene):
    def __init__(self, core):
        super().__init__(core)
        self.options = ["Start Game", "Options", "Exit"]
        self.selected_index = 0

    def handle_input(self, event):
        if event.type == EventType.MENU_UP:
            self.selected_index = max(0, self.selected_index - 1)
        elif event.type == EventType.MENU_DOWN:
            self.selected_index = min(len(self.options) - 1, self.selected_index + 1)
        elif event.type == EventType.MENU_SELECT:
            self._handle_selection()

    def _handle_selection(self):
        selection = self.options[self.selected_index].lower()
        if "exit" in selection:
            from windfall.core import WindfallEvent, EventType
            self.core.post_event(WindfallEvent(EventType.QUIT))
        elif "start" in selection:
            # We'll add scene switching logic here next!
            pass

    def render(self, renderer):
        renderer.render_menu(self.options, self.selected_index)