aainu = [7,5,3]
n = len(aainu)


for i in range(n):
    mini = i
    
    for j in range(i+1,n):
        if aainu[i] > aainu[j]:
           
            mini = j
    (aainu[i],aainu[mini])= (aainu[mini],aainu[i])
print(aainu)


