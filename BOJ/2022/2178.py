import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
arr = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    arr2 = sys.stdin.readline()
    for j in range(m):
        arr[i][j] = int(arr2[j])
# print(arr)

def DFS(i,j):
    myQueue = deque()
    myQueue.append((i,j))
    visited[i][j] = True

    while myQueue:
        now = myQueue.popleft()
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            if x>=0 and y>=0 and x<n and y<m:
                if arr[x][y]==1 and visited[x][y]!=True:
                    visited[x][y] = True
                    myQueue.append((x,y))
                    arr[x][y] = arr[now[0]][now[1]]+1

DFS(0,0)

print(arr[n-1][m-1])
