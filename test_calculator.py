import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
