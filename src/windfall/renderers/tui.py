from blessed import Terminal

class TUIRenderer:
    def __init__(self):
        self.term = Terminal()

    def setup(self):
        print(self.term.enter_fullscreen())
        print(self.term.hide_cursor())
        print(self.term.clear()) # Clear once at the start

    def render_menu(self, options, selected_index):
        # We only draw the menu at the center
        cx, cy = self.term.width // 2, self.term.height // 2
        
        # Header
        print(self.term.move_xy(cx - 10, cy - 4) + self.term.bold_teal("WINDFALL ENGINE"))
        print(self.term.move_xy(cx - 12, cy - 3) + self.term.darkgray("─" * 24))

        # Menu Options
        for i, option in enumerate(options):
            color = self.term.black_on_teal if i == selected_index else self.term.normal
            text = f" > {option} < " if i == selected_index else f"   {option}   "
            print(self.term.move_xy(cx - 10, cy + i) + color(text))

        # Footer
        footer = "W/S to Navigate | Q to Quit"
        print(self.term.move_xy(cx - len(footer)//2, self.term.height - 2) + self.term.darkgray(footer))

    def get_input(self):
        with self.term.cbreak():
            val = self.term.inkey(timeout=0.05) # Small timeout for responsiveness
            return val.code if val.is_sequence else val