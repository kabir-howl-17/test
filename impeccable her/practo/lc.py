n = 6
x = 2
y= 3
z = 4

outcome = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                ls = [i,j,k]
                outcome.append(ls)
print(outcome)

print(25//2)