n = 3
a = 1
while a > 0:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print("*", end = "  ")
                a = a+1
            print()
