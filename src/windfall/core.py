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

	# --- ADD THIS: The public update call ---
	def update(self):
		"""Process one tick of the engine."""
		self._process_events()

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