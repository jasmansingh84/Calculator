import math
import csv

def Add(x, y):
    x = int(x)
    y = int(y)
    z = x + y
    return z


def Subtract(x, y):
    x = int(x)
    y = int(y)
    z = y - x
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
    z= math.sqrt(x)
    return z

class Calculator:
    result = 0


    def __init__(self):
        pass

    def Add(self, x, y):
        self.result = Add(x, y)
        return self.result


    def Subtract(self, x, y):
        self.result = Subtract(x, y)
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


