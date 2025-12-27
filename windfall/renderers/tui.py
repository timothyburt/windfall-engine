from blessed import Terminal
from windfall.core import WindfallEvent, EventType

class TUIRenderer:
	def __init__(self):
		self.term = Terminal()

	def setup(self):
		print(self.term.enter_fullscreen())
		print(self.term.hide_cursor())
		print(self.term.clear())

	def render_menu(self, options, selected_index):
		cx, cy = self.term.width // 2, self.term.height // 2
		
		# Header
		print(self.term.move_xy(cx - 10, cy - 4) + self.term.bold_teal("WINDFALL ENGINE"))
		print(self.term.move_xy(cx - 12, cy - 3) + self.term.darkgray("─" * 24))

		# Menu Options
		for i, option in enumerate(options):
			# The Fix: Use format strings to avoid the 'not callable' error
			if i == selected_index:
				text = f"{self.term.black_on_teal} > {option} < {self.term.normal}"
			else:
				text = f"{self.term.normal}   {option}   "
			
			print(self.term.move_xy(cx - 10, cy + i) + text)

		# Footer
		footer = "W/S to Navigate | ENTER to Select | Q to Quit"
		print(self.term.move_xy(cx - len(footer)//2, self.term.height - 2) + self.term.darkgray(footer))

	def get_input(self):
		with self.term.cbreak():
			val = self.term.inkey(timeout=0.1)
			
			if not val:
				return None

			# Translation Layer: Hardware -> Engine Event
			if val.lower() == 'w' or val.code == self.term.KEY_UP:
				return WindfallEvent(EventType.MENU_UP)
			
			if val.lower() == 's' or val.code == self.term.KEY_DOWN:
				return WindfallEvent(EventType.MENU_DOWN)
			
			if val.code == self.term.KEY_ENTER or val == '\n':
				return WindfallEvent(EventType.MENU_SELECT)
			
			if val.lower() == 'q':
				return WindfallEvent(EventType.QUIT)

			return None

	def teardown(self):
		print(self.term.normal_cursor())
		print(self.term.exit_fullscreen())