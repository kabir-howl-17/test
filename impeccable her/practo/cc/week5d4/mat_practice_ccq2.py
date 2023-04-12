'''Q - 2) Write a program to print sum of border elements of a square Matrix'''

mat = [[1, 2, 3, 4], 
       [4, 5, 6, 5],
       [7, 8, 9, 6],
       [4, 9, 8, 7]]

#Sum of border elements = 1+2+3+4+5+6+7+8+9+4+7+4 = 60
n = len(mat)
m = len(mat[0])
sum = 0

for i in range(n):
    for j in range(m):
        if i == 0:
            sum = sum+ mat[i][j]
        elif j == n-1:
            sum = sum+mat[i][j]
        elif i == n-1:
            sum = sum+mat[i][j]
        elif j == 0:
            sum = sum + mat[i][j]
        else:
            sum = sum+0
print(sum)

           

