#finding even odd with & operator
'''

n = int(input("enter your number here=  "))
 
if (n & 1) == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')


'''
#checking if two numbers have opposite signs(i.e negative positive)

x = int(input("enter first number = "))
y = int(input("enter second number = "))
 
print(f'{x} in binary is {bin(x)}')
print(f'{y} in binary is {bin(y)}')
 
# true if `x` and `y` have opposite signs
checkitcutu = ((x ^ y) < 0)
 
if checkitcutu is True:
    print(f'{x} and {y} have opposite signs')
else:
    print(f'{x} and {y} don\'t have opposite signs')
 
