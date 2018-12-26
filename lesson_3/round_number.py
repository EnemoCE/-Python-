number = float(input())
ndigits = int(input())
def my_round(number,ndigits):
    number = str(number)
    number = number.split('.')
    if ndigits == 0 :
        return int(number[0])
    else:
        b = number[1][:(ndigits+1)]
        if int(b[-1]) >= 5 :
            b = b[:(ndigits-1)]+str(int(b[ndigits])+1)
        else:
            b = b[:ndigits]
        J='.'
        return float(J.join([number[0],b]))
print(my_round(number,ndigits))
    
