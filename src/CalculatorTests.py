import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


    def test_add(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)


    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(1, 1), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(1, 1), 1)
        self.assertEqual(self.calculator.result, 1)

if __name__ == '__main__':
    unittest.main()