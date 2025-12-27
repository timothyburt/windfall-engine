import time
from windfall.core import WindfallCore
from windfall.renderers.tui import TUIRenderer

def main():
    # 1. Initialize the "Eyes" (TUI)
    renderer = TUIRenderer()
    
    # 2. Initialize the "Brain" (Core)
    engine = WindfallCore(renderer)
    
    print("Pre-flight check complete. Launching Windfall Engine...")
    time.sleep(1) # Just for the drama
    
    # 3. Start the engine loop
    engine.run()

if __name__ == "__main__":
    main()