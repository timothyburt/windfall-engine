from collections import deque
from windfall.engine.events.events import WindfallEvent, EventType
from windfall.engine import SplashScene

class WindfallCore:
	def __init__(self, renderer):
		self.renderer = renderer
		self.scene_stack = [SplashScene(self)]
		self.running = True
		self.event_queue: deque[WindfallEvent] = deque()
		
		# Start with Splash instead of Menu to trigger the boot sequence
		self.scene_stack = [SplashScene(self)]

	@property
	def active_scene(self):
		"""Returns the scene currently at the top of the stack."""
		return self.scene_stack[-1] if self.scene_stack else None

	def post_event(self, event: WindfallEvent):
		self.event_queue.append(event)

	def update(self):
		# Phase 1: Clear the event queue (Input)
		while self.event_queue:
			event = self.event_queue.popleft()
			if event.type == EventType.QUIT:
				self.running = False
				return
			if self.active_scene:
				self.active_scene.handle_input(event) # This handles your 'Enter' skip

		# Phase 2: Logic Pulse (Timers/Animations)
		# THIS MUST BE OUTSIDE THE WHILE LOOP
		if self.active_scene:
			self.active_scene.update()
				
	def change_scene(self, new_scene):
		"""Replaces the entire stack with the new scene."""
		self.scene_stack = [new_scene]
		# Clear the screen once during the transition to prevent ghosting
		print(self.renderer.term.clear, end="")