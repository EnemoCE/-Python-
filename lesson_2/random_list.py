import random 
n = input('Требуемая длина списка: ')
ls = [random.randint(-100,100)+k*0 for k in range(n)]
print(ls)
