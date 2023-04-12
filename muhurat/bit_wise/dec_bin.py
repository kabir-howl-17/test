def d2b(num):
     
    if num >= 1:
        d2b(num // 2)
    print(num % 2, end = '')


num = 10
d2b(num)