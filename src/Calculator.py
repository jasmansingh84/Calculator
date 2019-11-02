import math
import csv

def Add(x, y):
    x = int(x)
    y = int(y)
    z = x + y
    return z


def Subtract(x, y):
    a = int(x)
    b = int(y)
    c = b - a
    return c

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
    z= math.sqrt(x)
    return z

class Calculator:
    result = 0


    def __init__(self):
        pass

    def Add(self, x, y):
        self.result = Add(x, y)
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
        return self.result

    def sqrt(self, x):
        self.result = math.sqrt(x)
        return self.result


