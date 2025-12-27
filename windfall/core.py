from collections import deque
from .events import WindfallEvent, EventType

class WindfallCore:
	def __init__(self):
		self.running = True
		# The engine's nervous system: a thread-safe FIFO queue
		self.event_queue: deque[WindfallEvent] = deque()

		# UI State
		self.menu_options = ["Start Engine", "Settings", "Exit"]
		self.selected_index = 0
		self.needs_redraw = True

	# --- ADD THIS: The entry gate ---
	def post_event(self, event: WindfallEvent):
		"""Standard way to inject events into the engine."""
		self.event_queue.append(event)

	def update(self):
		while self.event_queue:  # This is the 'Pythonic' way to check if a deque has items
			event = self.event_queue.popleft()

			if event.type == EventType.MENU_UP:
				self.selected_index = max(0, self.selected_index - 1)

			elif event.type == EventType.MENU_DOWN:
				self.selected_index = min(len(self.menu_options) - 1, self.selected_index + 1)

			elif event.type == EventType.QUIT:
				self.running = False  # This breaks the 'while core.running' loop in main.py

	def _process_events(self):
		"""Drains the queue and directs traffic."""
		while self.event_queue:
			event = self.event_queue.popleft()
			self._handle_event(event)

	def _handle_event(self, event: WindfallEvent):
		"""The logic brain: deciding what happens when an event fires."""
		if event.type == EventType.QUIT:
			self.running = False
		elif event.type == EventType.MENU_UP:
			self.selected_index = (self.selected_index - 1) % len(self.menu_options)
			self.needs_redraw = True
		elif event.type == EventType.MENU_DOWN:
			self.selected_index = (self.selected_index + 1) % len(self.menu_options)
			self.needs_redraw = True