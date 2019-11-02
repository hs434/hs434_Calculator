
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


