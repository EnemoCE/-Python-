import math as mt
l1 = input('Введите элементы списка через пробел: ')
l1 = l1.split()
l1 = [int(k) for k in l1]
l2 = []
for k in l1 :
    root = k**0.5
    if type(root) != complex:
        if root == mt.floor(root):
            l2.append(int(root))
print(l2)
