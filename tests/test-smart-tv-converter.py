import unittest
from src.smart_tv_converter import SmartTVConverter

class TestSmartTVConverter(unittest.TestCase):
    def setUp(self):
        self.converter = SmartTVConverter("Test TV", 32)

    def test_detect_tv(self):
        self.converter.detect_tv()
        self.assertIsNotNone(self.converter.system_info)
        self.assertEqual(self.converter.tv_model, "Test TV")
        self.assertEqual(self.converter.screen_size, 32)

    def test_install_apps(self):
        self.converter.install_apps()
        self.assertGreater(len(self.converter.installed_apps), 0)

    def test_add_free_channels(self):
        self.converter.add_free_channels()
        self.assertGreater(len(self.converter.free_channels), 0)

    def test_add_free_streaming_apps(self):
        self.converter.add_free_streaming_apps()
        self.assertGreater(len(self.converter.free_streaming_apps), 0)

    def test_calculate_total_size(self):
        self.converter.install_apps()
        self.converter.add_free_streaming_apps()
        total_size = self.converter.calculate_total_size()
        self.assertGreater(total_size, 0)

if __name__ == '__main__':
    unittest.main()
