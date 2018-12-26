a = int(input())
def lucky_ticket(number) :
    a = str(number)
    b1 = [ int(i) for i in a[0:3]]
    b2 = [ int(i) for i in a[3:6]]
    if sum(b1) == sum(b2):
        return True
    else :
        return False
print(lucky_ticket(a))
