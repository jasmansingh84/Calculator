def addition(x, y):
    z = x + y
    return z


def subtraction(x, y):
    z = x - y
    return z


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