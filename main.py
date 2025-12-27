import time
from windfall.renderers.tui import TUIRenderer
from windfall.core import WindfallCore

def main():
    # 1. Initialize the components
    tui = TUIRenderer()
    core = WindfallCore()
    
    tui.setup()
    
    try:
        while core.running:
            # 2. Input Phase: Capture hardware signal and translate to Event
            event = tui.get_input()
            
            # 3. Processing Phase: Feed the event into the Core
            if event:
                core.post_event(event)
            
            # 4. Update Phase: The Core processes the queue and updates logic
            core.update()
            
            # 5. Render Phase: Show the updated state
            # (Assuming core has a list of options and the current index)
            tui.render_menu(core.menu_options, core.selected_index)
            
            # 6. Heartbeat: Maintain a steady frame rate (approx 30 FPS)
            time.sleep(0.03)
            
    except KeyboardInterrupt:
        pass
    finally:
        # 7. Cleanup: Restore the terminal settings
        tui.teardown()

if __name__ == "__main__":
    main()