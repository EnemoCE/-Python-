max = 0
a = int(input())
for c in str(a):
    if int(c) > max:
        max = int(c)
print(max)