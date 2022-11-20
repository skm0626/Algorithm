n,k = map(int,input().split())
coin = []
answer = 0
for i in range(n):
    c = int(input())
    coin.append(c)

for i in range(n-1,-1,-1):
    if coin[i]<=k:
        answer += k//coin[i]
        k = k%coin[i]
print(answer)
