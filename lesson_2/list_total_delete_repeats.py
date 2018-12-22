l1 = input('Введите элементы списка через пробел: ')
l1 = l1.split()
l1 = [int(k) for k in l1]

for r in l1:
    if l1.count(r) > 1:
        while r in l1 :
            l1.remove(r)
print(l1)

#альтернативный более длинный код...
'''
li = list(l1)
for p in list(set(l1)):
    li.remove(p)
li = list(set(li))
for in li:
    while t in l1:
        l1.remove(t)
print(l1)
'''
