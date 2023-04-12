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

st = input("jaldi= ")
n = len(st)
def ct(st, h):
    n = len(st)
  

    if n == 0:
        return 0
    if n == 1:
        return int(st[0])+(h*10)
    else:
        h = int(st[0])+ (h*10)
        return (ct(st[1:], h))

b = ct(st, 0)  
print(b+1) 