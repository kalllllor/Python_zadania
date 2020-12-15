import math
from math import sqrt

class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag
    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    
    def __sub__(self,other):
        return Complex(self.real-other.real,self.imag-other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.real)
    
    def __div__(self, other):
        divisor = (other.real**2 + other.imag**2)
        return Complex((self.real * other.real) -
        (self.imag * other.imag)/divisor,
        (self.imag * other.real) + (self.real * other.imag)/divisor)

    def __abs__(self):
        new = (self.real**2 + (self.imag**2)*-1)
        return Complex(sqrt(new.real))