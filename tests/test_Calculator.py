import unittest

from src.calculator.calculator import Calculator
from src.Reader import reader


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        file = reader("Unit_Test_Addition.csv")
        print("TESTING ADDITION")
        for row in file:
            result = float(row[2])
            # print('---->: {0:4} +  {1:4} =  {2:4}'.format(row[0], row[1], row[2]))
            self.assertEqual(self.calculator.add(row[0], row[1]), float(row[2]))
            self.assertEqual(self.calculator.result, result)
            # self.assertEqual(self.calculator.add(5, 6), 11)
        print("PASSED")
        file.clear()
        print("\n")

    def test_subtraction(self):
        file = reader("Unit_Test_Subtraction.csv")
        print("TESTING SUBTRACTION")
        for row in file:
            # print('---->: {0:4} -  {1:4} =  {2:4}'.format(row[1], row[0], row[2]))
            self.assertEqual(self.calculator.subtract(row[0], row[1]), float(row[2]))
            # self.assertEqual(self.calculator.subtract(5, 6), 1)
        print("PASSED")
        file.clear()
        print("\n")

    def test_multiplication(self):
        file = reader("Unit_Test_Multiplication.csv")
        print("TESTING MULTIPLICATION")
        for row in file:
            result = float(row[2])
            # print('---->: {0:4} x  {1:4} =  {2:4}'.format(row[0], row[1], row[2]))
            self.assertEqual(self.calculator.multiply(row[0], row[1]), float(row[2]))
            # self.assertEqual(self.calculator.multiply(5, 6), 30)
        print("PASSED")
        file.clear()
        print("\n")

    def test_division(self):
        file = reader("Unit_Test_Division.csv")
        print("TESTING DIVISION")
        for row in file:
            result = float(row[2])
            # print('---->: {0:4} / {1:4} =  {2:4}'.format(row[1], row[0], row[2]))
            self.assertEqual(self.calculator.divide(row[0], row[1]), float(row[2]))
            # self.assertEqual(self.calculator.divide(6, 30), 5)
        print("PASSED")
        file.clear()
        print("\n")

    def test_square(self):
        file = reader("Unit_Test_Square.csv")
        print("TESTING SQUARE")
        for row in file:
            result = float(row[1])
            # print('---->: {0:4} ^ {1:2} =  {2:4}'.format(row[0], 2, row[1]))
            self.assertEqual(self.calculator.square(row[0]), float(row[1]))
            self.assertEqual(self.calculator.result, result)
            # self.assertEqual(self.calculator.square(5), 25)
        print("PASSED")
        file.clear()
        print("\n")

    def test_square_root(self):
        file = reader("Unit_Test_Square_Root.csv")
        print("TESTING SQUARE ROOT")
        for row in file:
            result = float(row[1])
            # print('---->: Square Root of {0:4} =  {1:4}'.format(row[0], row[1]))
            self.assertAlmostEqual(self.calculator.square_root(row[0]), float(row[1]))
            self.assertAlmostEqual(self.calculator.result, result)
            # self.assertEqual(self.calculator.square_root(100), 10)
        print("PASSED")
        file.clear()
        print("\n")
