a = [8,5,6,3,9,1]
l = len(a)
print(a[0])
c = [ ]
print(l)
for i in range(len(a)):
    mini = a[0]
    minient = 0
    for i in range(len(a)): #step 1
        if mini > a[i] :
            mini = a[i]
            minient = i

    c.append(a[minient])    
    a.remove(a[minient])

print(c)
print(a)
print(type(a))






