names = []
with open('fruits.txt', 'r') as f:
    for line in f:
        if len(line.strip()) :
            k = line.split()
            J = ' '
            k = J.join(k)+'\n'
            name = 'fruits_'+k[0]+'.txt'
            if name not in names:
                names.append(name)
                with open(name, 'w') as f:
                    f.write(k)
            else:
                with open(name, 'a') as f:
                    f.write(k)
                        
