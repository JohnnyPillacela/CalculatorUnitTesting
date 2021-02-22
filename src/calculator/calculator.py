from src.operations.operations import Operations


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = Operations.addition(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = Operations.subtraction(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = Operations.multiply(x, y)
        return self.result

    def divide(self, x, y):
        self.result = round(Operations.division(x, y), 9)
        return self.result

    def square(self, x):
        self.result = Operations.square(x)
        return self.result

    def square_root(self, x):
        self.result = Operations.square_root(x)
        return self.result
