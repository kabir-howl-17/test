def dd(num):
    benda = num
    k = 0
    if num == 0:
        return k
    if benda % (num%10) == 0:
        k = k+1
    dd(benda//10)
    


    

num = 121
print(dd(num))



