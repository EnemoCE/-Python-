a = float(input('Введите коэффициенты a,b,c квадратного уравнения:'))
b = float(input())
c = float(input())
D = b**2-4*a*c
k = -b/(2*a)
if D == 0 :
    print('Единственный корень уравнения:',k)
else: 
    r1 = k+D**0.5
    r2 = k-D**0.5
    print('Корни уравнения:',r1,r2)