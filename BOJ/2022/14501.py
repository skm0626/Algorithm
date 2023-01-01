import sys
n = int(sys.stdin.readline())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1,n+1):
    t[i],p[i] = map(int,sys.stdin.readline().split())

dp = [0]*(n+2)
for i in range(n,0,-1):
    if (t[i]+i > n+1):
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],dp[i+t[i]]+p[i])

print(dp[1])
