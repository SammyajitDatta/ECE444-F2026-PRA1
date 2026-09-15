import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.utils = utils()

    # reversed tests
    def test_reversed_integer(self):
        self.assertEqual(self.utils.reversed(1234), 4321)
        self.assertEqual(self.utils.reversed(-1000), -1)

    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            self.utils.reversed(12.34)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            self.utils.reversed("hello")

    # formatter tests
    def test_formatter_integer(self):
        self.assertEqual(self.utils.formatter(10), ("0b1010", "0o12"))

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            self.utils.formatter(10.5)

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            self.utils.formatter("hello")


if __name__ == "__main__":
    unittest.main()