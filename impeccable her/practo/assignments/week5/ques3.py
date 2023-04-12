blue = [12,6,8,5]    
p = False
for i in range(len(blue)):
    if blue[i]*2 in blue and blue.index(blue[i]*2) != i:
            p = True

print(p)