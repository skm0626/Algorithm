INF = int(1e9)
n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)] # 도시번호가 1부터 시작이라서 0번째 인덱스는 뺄거임 -> 결국 쓰는건 n개지만 0을 제외하고 n개 여야하니까 n+1

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            graph[i][j]=0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for p in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][p]+graph[p][j])

print(graph[1][k]+graph[k][x])
