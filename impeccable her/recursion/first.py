def rec(i):
    a = 0
    i = i+1
    if i %17 == 0:
        a= i+23
        return a
       
    
    return a+rec(i+1)
    
        

a = rec(100)
print(a)