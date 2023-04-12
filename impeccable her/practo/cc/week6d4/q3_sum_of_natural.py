'''Q-3 ) Given a number n, find sum of first n natural numbers:(5 marks)
Examples :
Input : 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15
Input : 7
Output : 28
Explanation : 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28'''


#iterative way 
n = int(input("enter inu till you want sum of == "))
sum = 0

for i in range(1, n+1):
    sum = sum+i
print(sum)

#recursive way 
def naturalsum(n,x):
    if n == 1:
        return x
    x = x+n
    return naturalsum(n-1,x)
    


if __name__ == "__main__":
    num = int(input("enter aainu till you want sum of == "))

    blue = naturalsum(n,1)
    print(blue)
