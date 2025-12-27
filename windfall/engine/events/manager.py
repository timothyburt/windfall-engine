class EventManager:
    """
    Future home of the engine's event bus.
    Will handle internal signals, input events, and state changes.
    """
    def __init__(self):
        self.listeners = {}

    def emit(self, event_name, data=None):
        # Placeholder for event broadcasting
        pass