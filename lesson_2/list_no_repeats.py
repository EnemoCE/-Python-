l1 = input('Введите элементы списка через пробел: ')
l1 = l1.split()
l1 = [int(k) for k in l1]
l2 = list(set(l1))
print(l2)
