l1 = input('Введите элементы первого списка через пробел: ')
l1 = l1.split()
l1 = [int(k) for k in l1]
l2 = input('Введите элементы второго списка через пробел: ')
l2 = l2.split()
l2 = [int(k) for k in l2]

'''
a = []
for n in l1 :
    for k in l2:
        if n == k:
            a.append(n) 
            
for f in set(a) :
    while f in l1 :
        l1.remove(f)
print(l1)
'''
l_1=set(l1)
l_2=set(l2)
l_1=l_1 & l_2
for f in l_1 :
    while f in l1 :
        l1.remove(f)
print(l1)
