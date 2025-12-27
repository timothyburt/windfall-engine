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
			event = tui.get_input()
			if event:
				core.post_event(event)

			core.update()

			# Render whatever scene is currently active
			if core.active_scene:
				core.active_scene.render(tui)

			time.sleep(0.03)

	except KeyboardInterrupt:
		pass
	finally:
		# 7. Cleanup: Restore the terminal settings
		tui.teardown()

if __name__ == "__main__":
	main()