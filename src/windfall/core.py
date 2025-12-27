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
                # 1. Process Input
                key = self.renderer.get_input()
                if key == 'q':
                    self.running = False
                
                # 2. Update Logic (Future home of player movement, etc.)
                
                # 3. Render
                self.renderer.render("Windfall Engine: TUI Mode Active")
                
                time.sleep(1/60) 
        finally:
            # This ensures even if it crashes, the terminal is fixed
            self.renderer.teardown()
            print("Windfall Engine shut down safely. Stoke level maintained.")