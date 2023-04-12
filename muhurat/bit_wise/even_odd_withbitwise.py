'''n = int(input("enter the number = "))

if n&1 != 0:
    print(f"{n} is odd")
else:
    print(f"{n} is even")
'''
'''
b = 8 & 1
print(b)
print(bin(-16))

c = 7 ^ 9

a = 0b0111
d = -0b1001
e = 0b1110
f = a ^ d
print(f)'''



n = 0b0011
def count(n): 
    v = 0      
    while n > 0 :
        v = v + 1
        print(bin(n), bin(n-1))
        print(n-1)
        n = n & n-1
        
        
    return v    

vins = count(n)
print(vins)
print(bin(-1))


a = 7
b = 4
c = a  | b
print(c)


