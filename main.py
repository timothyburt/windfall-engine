import time
from windfall.engine.renderers.tui import TUIRenderer
from windfall.engine import WindfallCore

def main():
	# 1. Initialize the components
	tui = TUIRenderer()
	core = WindfallCore(tui)
	
	tui.setup()
	
	try:
		while core.running:
			# 1. Capture input
			event = tui.get_input() 
			if event: core.post_event(event)

			# 2. Run the logic pulse
			core.update() 

			# 3. Draw the frame
			if core.active_scene:
				core.active_scene.render(tui)

			time.sleep(0.016)

	except KeyboardInterrupt:
		pass
	finally:
		# 7. Cleanup: Restore the terminal settings
		tui.teardown()

if __name__ == "__main__":
	main()