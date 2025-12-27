import time

class WindfallCore:
    def __init__(self, renderer):
        self.renderer = renderer
        self.running = False

    def run(self):
        self.running = True
        self.renderer.setup()
        
        try:
            while self.running:
                self.renderer.render("Windfall Engine: TUI Mode Active")
                
                # Add a small delay (approx 60 FPS)
                time.sleep(1/60) 
        except KeyboardInterrupt:
            self.running = False
        finally:
            self.renderer.teardown()