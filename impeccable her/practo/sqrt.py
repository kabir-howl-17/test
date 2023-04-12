
for i in range(5):
    x = int(input("yhan dalo number= "))
    if x==0 or x==1: 
        print(x)
    max = x
    min = 0
    q = (min+max)//2
    while(min < max):
        c = q * q
        if c == x: 
            print(q)
        elif c < x: 
            min = q+1
        else: 
            max=q
        q=(min+max)//2
    print(q - 1)
