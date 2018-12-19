import numpy as np
a = float(input('Введите коэффициенты a,b,c квадратного уравнения:'))
b = float(input())
c = float(input())
r = np.roots([a, b, c])
if r[0] != r[1] :
    print('Корни уравнения:',r[0],r[1])
else:
    print('Единственный корень уравнения:',r[0])
    