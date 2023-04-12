mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9,10,11,12],
       [13,14,15,16]]

#print sum of rows as list(sum of each row as an element)


m = len(mat)
n = len(mat[0])
listrowsum = []
for i in range(m):
    sumrow = 0
    for j in range(n):
        sumrow = sumrow + mat[i][j]
    listrowsum.append(sumrow)
print(listrowsum)


#print sum of columns as list(sum of each column as an element)
m = len(mat)
n = len(mat[0])
listcolsum = []
for i in range(m):
    sumcol = 0
    for j in range(n):
        sumcol = sumcol + mat[j][i]
    listcolsum.append(sumcol)
print(listcolsum)
