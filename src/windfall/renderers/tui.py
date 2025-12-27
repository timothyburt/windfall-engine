from blessed import Terminal

class TUIRenderer:
    def __init__(self):
        self.term = Terminal()

    def setup(self):
        print(self.term.enter_fullscreen())
        print(self.term.hide_cursor())

    def render(self, message):
        print(self.term.clear())
        # Center the text
        with self.term.location(self.term.width // 2 - len(message) // 2, self.term.height // 2):
            print(self.term.bold_teal(message))
        
        # Add a footer instruction
        with self.term.location(0, self.term.height - 1):
            print(self.term.center("Press 'q' to Exit Safely"))

    def get_input(self):
        # cbreak() allows us to read one char at a time
        # timeout=0 makes it non-blocking
        with self.term.cbreak():
            val = self.term.inkey(timeout=0)
            return val.lower() if val else None

    def teardown(self):
        print(self.term.normal_cursor())
        print(self.term.exit_fullscreen())