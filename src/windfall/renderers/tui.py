from blessed import Terminal

class TUIRenderer:
    def __init__(self):
        self.term = Terminal()

    def setup(self):
        print(self.term.enter_fullscreen())
        print(self.term.hide_cursor())
        print(self.term.clear())

    def render_menu(self, options, selected_index):
        cx, cy = self.term.width // 2, self.term.height // 2
        
        # Header
        print(self.term.move_xy(cx - 10, cy - 4) + self.term.bold_teal("WINDFALL ENGINE"))
        print(self.term.move_xy(cx - 12, cy - 3) + self.term.darkgray("─" * 24))

        # Menu Options
        for i, option in enumerate(options):
            # The Fix: Use format strings to avoid the 'not callable' error
            if i == selected_index:
                text = f"{self.term.black_on_teal} > {option} < {self.term.normal}"
            else:
                text = f"{self.term.normal}   {option}   "
            
            print(self.term.move_xy(cx - 10, cy + i) + text)

        # Footer
        footer = "W/S to Navigate | ENTER to Select | Q to Quit"
        print(self.term.move_xy(cx - len(footer)//2, self.term.height - 2) + self.term.darkgray(footer))

    def get_input(self):
        with self.term.cbreak():
            val = self.term.inkey(timeout=0.1)
            # Handle both string characters and special codes (like Enter)
            if val.is_sequence:
                return val.code
            return val.lower() if val else None

    def teardown(self):
        print(self.term.normal_cursor())
        print(self.term.exit_fullscreen())