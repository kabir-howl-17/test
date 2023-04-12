#q2
'''find the largest and second largest number in a list without using inbuilt functions'''

A = [1,3,4,5,8,1,2,3,4,9,6,9]

max = A[0]
for i in A:
    if i>max:
        max = i
print(f"largest in list A is {max}")
#now as we know the max so we can use it to obtain second largest
max = 9
secmax = A[0]
for i in A:
    if i>secmax and i <max:
        secmax = i
print(f"second largest in list A is {secmax}")