import math
from decimal import getcontext, Decimal

def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a*b
    return c

def division(a, b):
    c = b / a
    return c

def squarecalc(a):
    a = int(a)
    c = a*a
    return c

def squarerootcalc(a):
    getcontext().prec = 10
    c = Decimal(a).sqrt()
    return c


class Calculator:
    result = 0

    def add(self,a, b):
        self.result =  addition(a, b)
        return self.result

    def subtract(self,a,b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self,a,b):
        self.result = multiplication(a,b)
        return self.result

    def divide(self,a,b):
        self.result = division(a,b)
        return self.result

    def square(self,a):
        self.result = squarecalc(a)
        return self.result


    def squareroot(self,a):
        self.result = squarerootcalc(a)
        return self.result
