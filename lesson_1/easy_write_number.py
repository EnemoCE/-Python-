a = int(input('¬ведите целое число: '))
ln = len(str(a)) - 1
while ln >= 0:
    g = a // 10**ln
    print(g)
    a = a % 10**ln
    ln -= 1