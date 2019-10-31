import unittest
import csv
from CsvReader import CsvReader
from pprint import pprint
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
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(9, 3), 3)
        self.assertEqual(self.calculator.result, 3)

    def test_square(self):
        self.calculator.square(9)
        self.assertEqual(self.calculator.result, 81)

    def test_sqrt(self):
        self.calculator.sqrt(64)
        self.assertEqual(self.calculator.result, 8)

if __name__ == '__main__':
    unittest.main()