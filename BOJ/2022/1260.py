import sys
from collections import deque
n,m,s = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
visited1 = [False]*(n+1)
visited2 = [False]*(n+1)
myQueue = deque()

def DFS(v):
    visited1[v] = True
    print(v,end=' ')
    for i in arr[v]:
        if visited1[i]!=True:
            DFS(i)

def BFS(v):
    myQueue.append(v)
    visited2[v] = True
    while len(myQueue)>0:
        top = myQueue.popleft()
        print(top, end=' ')
        for i in (arr[top]):
            if visited2[i]!=True:
                visited2[i]=True
                myQueue.append(i)


for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(len(arr)):
    arr[i].sort()

DFS(s)
print()
BFS(s)
