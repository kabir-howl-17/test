"Display Fibonacci series up to 20 terms"



first = 0
second = 1
for i in range(20):
    print(first, end= "  ")
    next = first+second
    first = second
    second = next