import time

class WindfallCore:
    def __init__(self, renderer):
        self.renderer = renderer
        self.running = False
        self.menu_options = ["Start Engine", "Settings", "Credits", "Exit"]
        self.selected_index = 0
        self.needs_redraw = True

    def run(self):
        self.running = True
        self.renderer.setup()
        
        try:
            while self.running:
                if self.needs_redraw:
                    self.renderer.render_menu(self.menu_options, self.selected_index)
                    self.needs_redraw = False

                key = self.renderer.get_input()
                
                # Navigation
                if key == 'w' or key == self.renderer.term.KEY_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.menu_options)
                    self.needs_redraw = True
                elif key == 's' or key == self.renderer.term.KEY_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.menu_options)
                    self.needs_redraw = True
                
                # Selection Logic
                elif key == self.renderer.term.KEY_ENTER or key == '\n' or key == '\r':
                    selection = self.menu_options[self.selected_index]
                    if selection == "Exit":
                        self.running = False
                    else:
                        # Placeholder for future screens
                        self.renderer.render_menu([f"Selected: {selection}", "Back"], 0)
                        time.sleep(1)
                        self.needs_redraw = True

                elif key == 'q':
                    self.running = False
                
                time.sleep(0.01) 
        finally:
            self.renderer.teardown()