1 = input('¬ведите элементы списка через пробел: ')
l1 = l1.split()
l1 = [int(k) for k in l1]
l2 = []
for k in l1:
    if k % 2 == 0:
        el = k/4
    else:
        el = k*2
    l2.append(el)
print(l2)
