#how to convert an integer into a string

#simply by typecasting so that we can iterate over digits as considering them as the elements at string indexes


#for example 

n = 12345383733
m = str(n)
le = len(m)
print(le)
#here we calcuated the length of the string but if we try to calculate length of integer type puthon will throw error 
#lets see how
'''z = len(n)
print(z)'''
#TypeError: object of type 'int' has no len()
#as integer is considered to be a single unit as whole 

#so question is how print digits of a number separately
#there are many ways 
#1 by typecasting it to string and then again typecasting and printing the all index element of string 
# back into integer through a loop 
nums = 24225225
bums = str(nums)
print("output with string way")
for i in range(len(bums)):
    print(int(bums[i]))
#2 by using the mathematical operators in a creative way

num = 433733833

count = 10
res = []

while num != 0:
    bum = num%10
    num = num//count
    res.append(bum)
for i in range(len(res)-1,-1,-1):
    print(res[i])
    

# a recursive way of printing numbers in series

'''def nump(n):
    if n > 1:
        print(n) 
    else:
        return 1
        
    return (nump(n-1))

b = nump(10)
print(b)'''