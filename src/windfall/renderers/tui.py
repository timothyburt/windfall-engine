from blessed import Terminal

class TUIRenderer:
    def __init__(self):
        self.term = Terminal()

    def setup(self):
        print(self.term.enter_fullscreen())
        print(self.term.hide_cursor())

    def render(self, message):
        # Clears the screen and prints in the middle
        print(self.term.clear())
        with self.term.location(self.term.width // 2 - len(message) // 2, self.term.height // 2):
            print(self.term.bold_teal(message))

    def teardown(self):
        print(self.term.exit_fullscreen())
        print(self.term.normal_cursor())