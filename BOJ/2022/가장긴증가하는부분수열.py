import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [0]*n
for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i]+=1
print(max(dp))