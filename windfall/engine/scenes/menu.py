from windfall.engine import BaseScene
from windfall.engine.events.events import EventType

class MainMenuScene(BaseScene):
	def __init__(self, core):
		super().__init__(core)
		# 0 = LIBRARY (Left), 1 = FORGE (Right)
		self.selection = 0 
		self.options = ["LIBRARY", "FORGE"]

	def update(self):
		# The menu always needs input to function
		event = self.core.renderer.get_input()
		if event:
			self.handle_input(event)

	def handle_input(self, event):
		"""Processes A/D for horizontal navigation and ENTER for selection."""
		if event.type == EventType.MENU_LEFT:
			self.selection = 0
		elif event.type == EventType.MENU_RIGHT:
			self.selection = 1
		elif event.type == EventType.MENU_SELECT:
			self._execute_selection()
		elif event.type == EventType.QUIT:
			from windfall.engine.events.events import WindfallEvent
			self.core.post_event(WindfallEvent(EventType.QUIT))

	def _execute_selection(self):
		"""Determines which shard to 'Jack-in' to."""
		if self.selection == 0:
			# TODO: Transition to Library Scene
			pass
		elif self.selection == 1:
			# TODO: Transition to Forge/Wizard Scene
			pass

	def render(self, renderer):
		print(renderer.term.home, end="")
		term = renderer.term

		# Center coordinates
		mid_x = term.width // 2
		mid_y = term.height // 2

		# --- DRAW HEADER (Cyan) ---
		header = "=== WINDFALL SYSTEM DECK ==="
		renderer.draw_at(mid_x - len(header)//2, mid_y - 8, header, color=term.bold_cyan)

		# --- DRAW OPTION 1: LIBRARY (Teal) ---
		# If selected (0), use Yellow. If not, use Teal.
		lib_color = term.bold_yellow if self.selection == 0 else term.teal
		lib_box = [
			"╔═══════════════╗",

			"║    LIBRARY    ║",

			"╚═══════════════╝"
		]

		for i, line in enumerate(lib_box):
			renderer.draw_at(mid_x - 25, mid_y - 1 + i, line, color=lib_color)

		# --- DRAW OPTION 2: FORGE (Magenta) ---
		# If selected (1), use Yellow. If not, use Magenta.
		forge_color = term.bold_yellow if self.selection == 1 else term.magenta
		forge_box = [
			"╔═══════════════╗",

			"║     FORGE     ║",

			"╚═══════════════╝"
		]

		for i, line in enumerate(forge_box):
			renderer.draw_at(mid_x + 5, mid_y - 1 + i, line, color=forge_color)

		# --- DRAW DATA CABLE (Green) ---
		# This draws a line from the header to the selected box
		target_x = (mid_x - 17) if self.selection == 0 else (mid_x + 13)
		renderer.draw_at(target_x, mid_y - 5, "║", color=term.green)
		renderer.draw_at(target_x, mid_y - 4, "▼", color=term.green)

		# Display version near the header or footer
		renderer.draw_at(2, 1, f"CORE VER: {self.version}", color=renderer.term.darkgray)

		# --- FOOTER ---
		footer = "A / D to Navigate | ENTER to Jack-In"
		renderer.draw_at(mid_x - len(footer)//2, term.height - 3, footer, color=term.darkgray)