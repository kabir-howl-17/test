#sum of n numbers
'''n = int(input("enter the number = "))
c =0
for i in range(1,n+1):
    c = c+i
    print(c)'''

'''
def sums(n):
    if n == 3:
        return 3
    else :
        return n + sums(n-1)    






n = int(input("enter = "))
b = sums(n)
print(b)


# another rec 


n = int(input("enter your number= "))
m = int(input("enter your number= "))
def powersbd(n,m):
    if m == 0:
        return 1
    else :
        return n * powersbd(n,m-1)    

red = powersbd(n,m)
print(red)
'''
#print a given string in reverse order please inu mam i cant live without u 
st = input("enter your khuch bhi likho yaar= ")
k = len(st)-1
''''for i in range(k-1,-1,-1):
    print(st[i])'''

def Reversesting(st,k):
    if k == 0 :
        return st[0] 

    else :
        print(st[k],end="")
        return Reversesting(st,k-1)   

c = Reversesting(st,k)
print(c)