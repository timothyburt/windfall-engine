import time
from windfall.engine import BaseScene
from windfall.engine.events.events import EventType

# --- UI COMPONENTS ---

class SplashLogo:
	def __init__(self):
		self.alpha = 0.0  # Float for smooth math
		self.lines = [
			r" _      _           _  __        _  _ ",
			r"| | _  (_)_ __   __| |/ _| __ _ | || |",
			r"| |/ \ | | '_ \ / _` | |_ / _` || || |",
			r"| |\  || | | | | (_| |  _| (_| || || |",
			r"|_| \_||_|_| |_|\__,_|_|  \__,_||_||_|"
		]
		self.width = 38

	def update(self):
		if self.alpha < 1.0:
			self.alpha += 0.015

	def render(self, renderer, x, y):
		# Calculate fade color
		intensity = int(255 * max(0.0, min(1.0, self.alpha)))
		cyan_fade = renderer.term.color_rgb(0, intensity, intensity)
		
		for i, line in enumerate(self.lines):
			renderer.draw_at(x, y + i, line, color=cyan_fade)

class ProgressBar:
	def __init__(self, width):
		self.width = width
		self.progress = 0.0

	def update(self, elapsed, duration=4.0):
		self.progress = min(1.0, elapsed / duration)

	def render(self, renderer, x, y):
		filled_size = int(self.width * self.progress)
		bar_text = "█" * filled_size + "░" * (self.width - filled_size)
		# Explicitly set to Magenta to prevent color bleed
		renderer.draw_at(x, y, bar_text, color=renderer.term.magenta)

class DiagnosticLogger:
	def __init__(self, boot_logs):
		self.all_logs = boot_logs
		self.active_logs = []
		self.index = 0
		self.last_log_time = 0

	def update(self, elapsed):
		# Start logs after 0.8s delay
		if elapsed > 0.8 and self.index < len(self.all_logs):
			if time.time() - self.last_log_time > 0.3:
				self.active_logs.append(self.all_logs[self.index])
				self.index += 1
				self.last_log_time = time.time()

	def render(self, renderer, x, y):
		for i, log in enumerate(self.active_logs[-3:]):
			# Overwrite line to prevent ghosting
			clean_log = log.ljust(renderer.term.width - 10)
			log_color = renderer.term.green if "OK" in log else renderer.term.yellow
			renderer.draw_at(x, y + i, clean_log, color=log_color)

# --- MAIN SCENE ---

class SplashScene(BaseScene):
	def __init__(self, core):
		super().__init__(core)
		self.start_time = time.time()
		
		# Initialize sub-components
		self.logo = SplashLogo()
		self.progress_bar = ProgressBar(width=38)
		self.logger = DiagnosticLogger([
			"[ OK ] MOUNTING VIRTUAL FILESYSTEM...",
			"[ OK ] SYNCING NEURAL CORE [CYAN_PROTOCOL]...",
			"[ OK ] SCANNING LIBRARY SECTORS...",
			"[ !! ] WARNING: UNREGISTERED SHARDS DETECTED.",
			"[ OK ] INITIALIZING WINDFALL ENGINE...",
			"[ >> ] HANDSHAKE SUCCESS. WELCOME, ARCHITECT."
		])

	def update(self):
		elapsed = time.time() - self.start_time

		# Update all component logic
		self.logo.update()
		self.progress_bar.update(elapsed)
		self.logger.update(elapsed)

		# Auto-Transition logic
		if elapsed > 4.5:
			self._transition()

	def handle_input(self, event):
		# Allow skipping with Enter
		if event.type == EventType.MENU_SELECT:
			self._transition()

	def render(self, renderer):
		# Use home instead of clear to prevent flicker
		print(renderer.term.home, end="")
		
		term = renderer.term
		# Shared positioning math
		lx = (term.width // 2) - (self.logo.width // 2)
		ly = (term.height // 2) - 5

		# Render each piece
		self.logo.render(renderer, lx, ly)
		self.progress_bar.render(renderer, lx, ly + 6)
		self.logger.render(renderer, 4, term.height - 4)

		# Display version in the bottom right
		ver_text = f"v{self.version}"
		renderer.draw_at(renderer.term.width - len(ver_text) - 2, 
						renderer.term.height - 1, 
						ver_text, 
						color=renderer.term.darkgray)

	def _transition(self):
from windfall.engine import MainMenuScene
		self.core.change_scene(MainMenuScene(self.core))