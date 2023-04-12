n = int(input("no of rows you want in matrix = "))
m = int(input("no of columns you want in matrix= "))

mat = []

for i in range(n):
    mat.append([])
    for j in range(m):
        element = int(input(" enter the number for row {i} and colums {j} = "))
        mat[i].append(element)
print(mat)