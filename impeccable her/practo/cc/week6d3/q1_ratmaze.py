#rat maze
def ratmaze(i,j,n,m,maze):
    if i > n-1:
        return 0
    if j > m-1:
        return 0
    if maze[i][j]==1:
        return 0
    if i == n-1 and j == m-1:
        return 1
    
    ans = ratmaze(i+1,j,n,m,maze)+ratmaze(i,j+1,n,m,maze)
    return ans

maze = [[0,0,1,0],
        [0,0,1,1],
        [1,0,0,1],
        [0,1,0,0]]

n = len(maze)
m = len(maze[0])

res = ratmaze(0,0,n,m,maze)
print(f"there are {res} ways to reach the destination")