import numpy as np
a = float(input('������� ������������ a,b,c ����������� ���������:'))
b = float(input())
c = float(input())
r = np.roots([a, b, c])
if r[0] != r[1] :
    print('����� ���������:',r[0],r[1])
else:
    print('������������ ������ ���������:',r[0])
    