#intersection of two arrays 

num1 = [1,2,2,1]
num2 = [2,2]
num1.sort()
num2.sort()

res = []
i = 0
j = 0
while i < len(num1) and j < len(num2):
    if num1[i] < num2[j]:
        i = i+1
    elif num1[i]> num2[j]:
        j = j+1
    else:
        res.append(num1[i])
        i = i+1
        j = j+1
print(res)