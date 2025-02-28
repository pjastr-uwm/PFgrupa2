import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum_int(self):
        self.assertEqual(self.calculator.add(6, 7), 13)

    def test_sum_int_negative(self):
        self.assertNotEqual(self.calculator.add(6, 7), 20)

    def test_sum_float(self):
        self.assertAlmostEqual(self.calculator.add(0.1, 1e25), 1e25)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
