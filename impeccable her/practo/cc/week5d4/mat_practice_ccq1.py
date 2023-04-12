'''Q - 1) Write a program to print the sum of right diagonal of a matrix:'''

#1
mat =  [[1,2,3],
        [4,5,6],
        [7,8,9]]

m = len(mat)
n = len((mat)[0])
print(m,"X", n)

for i in range(m):
    for j in range(n):
        if ((i + j) == (n - 1)):
                print(mat[i][j], end = ", ")
print()
#2
bat =  [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]]
m = len(bat)
n = len((bat)[0])
print(m,"X", n)

for i in range(m):
    for j in range(n):
        if ((i + j) == (n - 1)):
                print(bat[i][j], end = ", ")

#3
print()
cat = [[1,2],
       [3,4],
       [5,6]]

m = len(cat)
n = len(cat[0])
print(m,"X",n)
for i in range(m):
    for j in range(n):
        if (i+j) == (n-1):    #for left diogonal condition will be if i == j
            print(cat[i][j], end= ",")
print()


