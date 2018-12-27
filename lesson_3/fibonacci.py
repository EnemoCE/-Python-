n = int(input())
m = int(input())
def fibonacci(n,m):
    a = 0
    b = 1
    i = 1
    list = []
    if m > 1:
        for k in range(m-1):
            c = a
            a = b
            b += c
            i += 1
            if i >= n:
                list.append(b)           
    else:
        list = [1]
    if n == 1:
        list.insert(0,1)        
    return list
print(fibonacci(n,m))
        
