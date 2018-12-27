co1 = {}
co2 = {}
fin = {}
with open('hours.txt', 'r') as f:
    for line in f:
        if len(line.strip()) > 0:
            k = [int(s) for s in line.split() if s.isdigit()]
            if k != []:
                J=' '
                name = J.join(line.split()[0:2])
                k,= k
                co1[name] = k
with open('money.txt', 'r') as f:
    for line in f:
        if len(line.strip()) > 0:
            k = [int(s) for s in line.split() if s.isdigit()]
            if k != []:
                J=' '
                name = J.join(line.split()[0:2])
                co2[name] = k
for key in co1.keys():
    z = (co1[key]/co2[key][1])
    if z > 1:
        v = ((z-1)*2+1)*co2[key][0]
    else:
        v = z*co2[key][0]
    fin[key] = int(v)
for key, value in fin.items():
    print(key,value)
