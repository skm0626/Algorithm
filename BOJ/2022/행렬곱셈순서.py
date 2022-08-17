import sys
n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for i in range(n)]
# print(arr)
dp = [[0]*n for i in range(n)]

for d in range(1,n): #자기 자신 제외
    for i in range(n-d):
        j = i+d
        # if i==j:
        #     continue
        # 최대로 만들어두기
        dp[i][j] = float('inf')
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+arr[i][0]*arr[k][1]*arr[j][1])
print(dp[0][-1])