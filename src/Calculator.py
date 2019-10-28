from math import *

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x*y
    return z

def divide(x, y):
    z = x/y
    return z

def square(x):
    z = x * x
    return z

def sqrt(x):
    math.sqrt(x)
    return z

class Calculator:
    result = 0


    def __init__(self):
        pass

    def add(self, x, y):
        self.result = add(x, y)
        return self.result


    def subtract(self, x, y):
        self.result = subtract(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = multiply(x, y)
        return self.result

    def divide(self, x, y):
        self.result = divide(x, y)
        return self.result

    def square(self, x):
        self.result = square(x)

    def sqrt(self, x):
        self.result = math.sqrt(x)