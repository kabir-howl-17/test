'''Q-2 ) Program for Sum of the digits of a given number:(5 marks)
Sample Input:
1234567
Sample output:28'''

#iterative way
n = int(input("enter aainu here=  "))
sums = 0

while (n > 0):
    res = n%10
    sums = sums + res
    n = n//10
print(sums)

#recursive way
def digsum(num, x):
    if num == 0:
        return x
    x = x + num%10
    return digsum(num//10, x)

#driver code
if __name__ == "__main__":
    num = int(input("enter inu here =  "))

    brew =  digsum(num,0)
    print(brew)

