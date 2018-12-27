import sympy as sp
x, y = sp.symbols('x y')
equation = '25/3+4/5'
expr = sp.sympify(equation)
a = int(expr)
b = expr - a
print(a,b)
