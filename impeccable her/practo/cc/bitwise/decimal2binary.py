def dec2bin(num):
    bina = ""
    while num > 0:
        remi = num%2
        bina = bina + str(remi)
        num = num//2

    return bina

num = 5
print(dec2bin(num))