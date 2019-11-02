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
        test_data = CsvReader('/src/addition_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_subtract(self):
        test_data = CsvReader('/src/subtraction_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply(self):
        test_data = CsvReader('/src/Multiply_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide(self):
        test_data = CsvReader('/src/division_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


def test_square(self):
    test_data = CsvReader('/src/square_test.csv').data
    pprint(test_data)
    for row in test_data:
        self.assertEqual(self.calculator.Square(row['Value 1']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrt(self):
        test_data = CsvReader('/src/square-root_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Square_root(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()