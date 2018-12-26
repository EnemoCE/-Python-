ls = list(map(chr, range(ord('А'), ord('Я')+1)))
co1 = {}
for i in ls:
    co1[i] = []
with open('fruits.txt', 'r') as f:
    for line in f:
        if len(line.strip()) > 0:
            k = line.split()
            for i in ls:
                if k[0][0] == i:
                    co1[i].append(k)
for i in ls:
    if co1[i] == []:
        ls.remove(i)
for i in ls:
    name = 'fruits_'+i+'.txt'
    with open(name, 'w') as f:
        an =''
        for t in co1[i]:
            J = ' '
            t = J.join(t)
            an = an+t+'\n'
        f.write(an)

