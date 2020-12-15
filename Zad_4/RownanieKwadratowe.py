import math
from typing import List


coefficients = []
abc =['a','b','c']

for i in range(0, 3):
    print('Podaj wspolczynnik '+ abc[i])
    ele = float(input())
    coefficients.append(ele) 

a = float(coefficients[0])
b = float(coefficients[1])
c = float(coefficients[2])

delta = float(b*b - 4*a*c)

if delta>0:
    x1 = (-b - math.sqrt(delta))/2*a
    x2 = (-b + math.sqrt(delta))/2*a

    print("Pierwiastek 1: %s" % (x1))
    print("Pierwiastek 2: %s" % (x2))
if delta==0:
    x0 =-b/2*a
if delta<0:
    cdelta = complex(delta)**0.5
    re=(-b-cdelta)/2*a
    im=(-b+cdelta)/2*a
    print("Czesc rzeczywista: %s" % (re))
    print("Czesc urojona: %s" % (im))