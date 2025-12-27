class WindfallCore:
    def __init__(self, renderer):
        self.renderer = renderer
        self.running = False

    def run(self):
        self.running = True
        self.renderer.setup()
        
        try:
            while self.running:
                # This is where game logic will go
                self.renderer.render("Windfall Engine: TUI Mode Active")
        finally:
            self.renderer.teardown()