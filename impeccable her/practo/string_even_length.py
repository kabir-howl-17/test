n = input(" enter a sentence=  ")
m = n.split()
#print(m)
for even in m:
    if len(even) % 2 == 0:
        print(even)
    else:
        continue

