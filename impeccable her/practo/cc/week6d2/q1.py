'''Q-1 ) Recursive implementation of atoi() function:(5 marks)
Atoi() function converts a string into an integer.
eg:
st = “1234” is a string.
if we perform,
st + 1
this results in error since “st” is a string and 1 is an integer, and,
st + “1”
this will append 1 into 1234. Giving us 12341.
write a function that converts the above variable ‘st’ into an integer (so that we
can perform mathematical operations on it).
Let’s call our function “myAtoiRecursive()”, it should,
myAtoiRecursive(st) + 1
should give us 1235 (that is 1234+1).
As shown in image below:
Sample input:
“1234”
Sample output:
1234'''


#iterative way
'''st = input("enter string to converted into str+1 = ")

n = len(st)
base = 1
strr = 0
for i in range(n-1,-1,-1):
    strr = strr+base*int(st[i])
    base = base*10
print(strr+1)'''

#recursive way


def huh(st, n):  
    if len(st) == 0:
        return 0
   
    if len(st) == 1:
        return int(st) + (n * 10)
         
    else:
        n = int(st[0]) + (n * 10)
        return (huh(st[1:], n))
 
   
st = input("enter only numbers bud=  ")
 
print(huh(st, 0)+1)

