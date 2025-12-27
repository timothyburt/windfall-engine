import unittest
from windfall.core import WindfallCore
from windfall.events import WindfallEvent, EventType

class TestNervousSystem(unittest.TestCase):
    def setUp(self):
        """Runs before every test."""
        self.engine = WindfallCore()

    def test_menu_navigation(self):
        """Test that MENU_UP/DOWN events change the selected index."""
        # Test Down
        self.engine.post_event(WindfallEvent(EventType.MENU_DOWN))
        self.engine.update()
        self.assertEqual(self.engine.selected_index, 1)

        # Test Up (Wrap back to 0)
        self.engine.post_event(WindfallEvent(EventType.MENU_UP))
        self.engine.update()
        self.assertEqual(self.engine.selected_index, 0)

if __name__ == "__main__":
    unittest.main()