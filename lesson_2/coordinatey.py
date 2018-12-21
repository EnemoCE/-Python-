import sympy as sp
x, y = sp.symbols('x y')
equation = 'y = -12x + 11111140.2121'
#семпай не понимает данную строку, ее нужно серьезно модифицировать
#программа решает любое уравнение вида y = ax + b где a,b - числа 
equation = equation.replace('y = ','')
equation = equation.replace('x','*x')
expr = sp.sympify(equation)
y = expr.subs(x,2.5)
print('y =',y)
