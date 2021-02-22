import math


class Operations:

    @staticmethod
    def addition(a, b):
        return float(a) + float(b)

    @staticmethod
    def subtraction(a, b):
        a = float(a)
        b = float(b)
        c = b - a
        return c

    @staticmethod
    def multiply(a, b):
        return float(a) * float(b)

    @staticmethod
    def division(a, b):
        try:
            result = float(b) / float(a)
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero")

    @staticmethod
    def square(a):
        return float(a) * float(a)

    @staticmethod
    def square_root(a):
        return math.sqrt(float(a))
