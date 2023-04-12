'''Q-4 ) [Bonus Question] Given two number x and y, find product using
recursion.
(3 extra marks)
Examples :
Input : x = 5, y = 2
Output : 10
Input : x = 100, y = 5
Output : 500'''

#fuck iterative direct recursive

def pro(x,y,z):
    if y == 0:
        return z
    z = z+x
    return pro(x,y-1,z)


x = int(input("enter the number= "))
y = int(input("enter the number you want to multiply x with= "))

prodcut = pro(x,y,0)
print(prodcut)