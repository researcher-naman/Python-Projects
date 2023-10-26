from ast import Return
from sympy import *


# Use sympy.Derivative() method for geting f'(x)

x = symbols('x')
expr = x**3 - 5*x + 1
expr_diff = Derivative(expr, x) 
defiex = expr_diff.doit()

# Printing F(x) and F'(x) for user

print("f(x) = " + str(expr))
print("\nSo the derivative of f(x) will  be")
print("\nf'(x) = " + str(defiex))
