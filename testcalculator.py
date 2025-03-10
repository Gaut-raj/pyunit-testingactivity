import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(3, 2), 5)
        self.assertEqual(Calculator().add(1, 2), 3)
    def test_subtract(self):
        self.assertEqual(Calculator().subtract(3, 2), 1)
        self.assertEqual(Calculator().subtract(5, 1), 4)
    def test_multiply(self):
        self.assertEqual(Calculator().multiply(3, 2), 6)
        self.assertEqual(Calculator().multiply(1, 2), 2)
    def test_divide(self):
        self.assertEqual(Calculator().divide(10, 2), 5)
        self.assertEqual(Calculator().divide(100, 10), 10)
if __name__ == '__main__':
    unittest.main()
