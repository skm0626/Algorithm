n = int(input())

dp = [0] * n

for i in range(1,n):
    dp[i] = dp[i-1]+1
    if i%2==0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%5==0:
        dp[i] = min(dp[i],dp[i//5]+1)
print(dp[n-1])
