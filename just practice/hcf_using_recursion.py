#highest common factor of twu numbers using recursion 

def hcf(x,y):

    if y == 0:
        return x
    else:
        return hcf(y,x%y)




x = int(input("enter first number= "))
y = int(input("enter second number= "))

b = hcf(x,y)
print(b)
