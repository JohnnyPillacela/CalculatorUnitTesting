import unittest

from src.calculator.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 6), 1)

    def test_addition(self):
        self.assertEqual(self.calculator.add(5, 6), 11)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(5, 6), 30)

    def test_division(self):
        self.assertEqual(self.calculator.divide(6, 30), 5)

    def test_square(self):
        self.assertEqual(self.calculator.square(5), 25)

    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(100), 10)
        '''
        test_data = CsvReader("Tests/Data/subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
        '''


