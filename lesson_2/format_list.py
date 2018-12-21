lst = ["яблоко", "банан", "киви", "арбуз"]
r = 0
for k in lst:
    r += 1
    print( r,'.{:>8}'.format(k),sep='')