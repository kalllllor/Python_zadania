import re
from LiczbyZespolone import Complex

brackets = re.compile('\([+-i\d]+\)')
operators = re.compile('\)[*+-]\(')
numbers = re.compile('[-]?\d+')

def parse_equation(string):
    values = re.findall(brackets, string)
    operation = re.findall(operators, string)[0][1]
    number1 = re.findall(numbers, values[0])
    number2 = re.findall(numbers, values[1])
    return Complex(int(number1[0]), int(number1[1])), \
           Complex(int(number2[0]), int(number2[1])), \
           operation
    pass

print("Format: (a+bi)*(c+di)")
print("Supported operations: +/-/*")
string = input('Equation: ')
comp1, comp2, operator = parse_equation(string)
if operator == '+':
    print(Complex.__add__(comp1,comp2))
elif operator == '-':
    print(Complex.__sub__(comp1,comp2))
elif operator == '*':
    print(Complex.__mul__(comp1,comp2))
elif operator == '/':
    print(Complex.__div__(comp1,comp2))
