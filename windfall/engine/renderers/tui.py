from blessed import Terminal
from windfall.engine.events.events import WindfallEvent, EventType

class TUIRenderer:
	def __init__(self):
		self.term = Terminal()

	def setup(self):
		print(self.term.enter_fullscreen())
		print(self.term.hide_cursor())
		print(self.term.clear())

	def clear(self):
		"""Wipes the terminal screen for the next frame."""
		# Using home + clear ensures we don't get flickering or ghosting
		print(self.term.home + self.term.clear, end="", flush=True)

	def draw_at(self, x, y, text, color=None):
		"""Draws text at coordinates. Resets terminal state to prevent color bleeding."""
		with self.term.location(x, y):			
			paint = color if color else self.term.normal
			# The structure {RESET}{NEW_COLOR}{TEXT}{RESET} is the industry standard for TUIs
			print(f"{self.term.normal}{paint}{text}{self.term.normal}", end="", flush=True)

	def get_input(self):
		"""Returns a WindfallEvent if a key is pressed, otherwise None."""
		with self.term.cbreak():
			val = self.term.inkey(timeout=0) # Non-blocking is mandatory here
			if not val:
				return None
			return self._map_key_to_event(val)

	def teardown(self):
		print(self.term.normal_cursor())
		print(self.term.exit_fullscreen())

	def _map_key_to_event(self, key):
		"""Translates raw terminal input into WindfallEvents."""
		from windfall.engine.events.events import WindfallEvent, EventType

		# Navigation
		if key.name == "KEY_UP" or key == "w":
			return WindfallEvent(EventType.MENU_UP)
		if key.name == "KEY_DOWN" or key == "s":
			return WindfallEvent(EventType.MENU_DOWN)
		if key.name == "KEY_LEFT" or key == "a":
			return WindfallEvent(EventType.MENU_LEFT)
		if key.name == "KEY_RIGHT" or key == "d":
			return WindfallEvent(EventType.MENU_RIGHT)

		# Selection / Interaction
		if key.name == "KEY_ENTER" or key == "\n" or key == "\r":
			return WindfallEvent(EventType.MENU_SELECT)

		# System
		if key == "q" or key == "Q" or key.name == "KEY_ESCAPE":
			return WindfallEvent(EventType.QUIT)

		return None