import unittest
from windfall.core import WindfallCore

class TestEngineCore(unittest.TestCase):
    def test_initial_state(self):
        """Verify the engine starts with the right defaults."""
        engine = WindfallCore()
        self.assertTrue(engine.running)
        self.assertEqual(engine.selected_index, 0)
        self.assertTrue(engine.needs_redraw)