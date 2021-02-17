from src.calculator.functions.Addition import addition
from src.calculator.functions.Subtraction import subtraction
from src.calculator.functions.Division import division
from src.calculator.functions.Multiply import multiply
from src.calculator.functions.Square import square
from src.calculator.functions.SquareRoot import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = addition(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = subtraction(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = multiply(x, y)
        return self.result

    def divide(self, x, y):
        self.result = round(division(x, y), 9)
        return self.result

    def square(self, x):
        self.result = square(x)
        return self.result

    def square_root(self, x):
        self.result = square_root(x)
        return self.result
