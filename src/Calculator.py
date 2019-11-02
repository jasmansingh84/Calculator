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

def Multiply(x, y):
    x = int(x)
    y = int(y)
    z = x * y
    return z

def Divide(x, y):
    x = int(x)
    y = int(y)
    z = y / x
    z = round(z, 9)
    return z

def Square(x):
    x = int(x)
    z = x ** 2
    return z


def Square_root(x):
    x = int(x)
    z = x ** 0.5
    if z > 10:
        z = round(z, 8)
    else:
        z = round(z, 9)

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

    def Multiply(self, x, y):
        self.result = Multiply(x, y)
        return self.result

    def Divide(self, x, y):
        self.result = Divide(x, y)
        return self.result

    def Square(self, x):
        self.result = Square(x)
        return self.result

    def Square_root(self, x):
        self.result = Square_root(x)
        return self.result


