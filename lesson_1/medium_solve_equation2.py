a = float(input('������� ������������ a,b,c ����������� ���������:'))
b = float(input())
c = float(input())
D = b**2-4*a*c
k = -b/(2*a)
if D == 0 :
    print('������������ ������ ���������:',k)
else: 
    r1 = k+D**0.5
    r2 = k-D**0.5
    print('����� ���������:',r1,r2)