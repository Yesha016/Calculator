def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a

def multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b

def division(a, b):
    return a / b

def square(a):
    return a ** 2

def squareroot(a):
    return a ** 0.5

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(a)
        return self.result


