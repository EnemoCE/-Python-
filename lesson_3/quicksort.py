# quick sort разбиение Хоара
l = input()
l = [ int(i) for i in l]
def quick_sort(l,fi = 0,la = len(l)-1):
    def qr(l,fi,la):
        op = l[int((fi+la)/2)]
        i = fi 
        j = la
        print(i)
        print(j)
        while i <= j :
            print("r")
            print(j)
            while l[i] < op :
                i += 1
            while l[j] > op:
                j -= 1
            if i <= j:
                if l[i] > l[j]:
                    print('ah,ep')
                    l[i],l[j] = l[j],l[i]
                i += 1
                j -= 1
        def rt_1():
            if i < la :
                fi = i
                qr(l,fi,la)
        def rt_2():
            if fi < j :
                print('r')
                la = j
                qr(l,fi,la)
        rt_1()
        rt_2()
    qr(l,fi,la)
    return l
print(quick_sort(l))


    
       
    
    
