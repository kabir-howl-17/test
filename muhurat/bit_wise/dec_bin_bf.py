def d2b(num):
    aaina = ""
    if num == 0 :
        return 0
    while num:
        ans += str(num&1)
        num = num >> 1
     
    aaina = aaina[::-1]
 
    return aaina