import numpy as np
a = []
for i in range(4):
    a.append([float(i) for i in input().split(',')])
a = np.array(a)
i = 0
if np.cross([a[0,0]-a[1,0],a[0,1]-a[1,1]],[a[2,0]-a[3,0],a[2,1]-a[3,1]]) == 0 :
    i +=1
if np.cross([a[0,0]-a[3,0],a[0,1]-a[3,1]],[a[2,0]-a[1,0],a[2,1]-a[1,1]]) == 0 :
    i +=1
if np.cross([a[0,0]-a[2,0],a[0,1]-a[2,1]],[a[1,0]-a[3,0],a[1,1]-a[3,1]]) == 0 :
    i+=1
if i == 2:
    print('Параллелограм')
else:
    print('Точки не являются вершинами параллелограма')
