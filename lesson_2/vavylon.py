n = input('Введите номер комнаты: ')
n = int(n)
su = 0
k = 0
floor = 0
while su < n :
    k += 1
    su += k**2
    floor += k
floor -= k
su -= k**2
n = n - su
p = [n//k,n%k]
if p[1] == 0 :
    floor = floor + p[0]
    num = k
else :
    floor = floor + p[0] + 1
    num = p[1]
print(floor,num)
