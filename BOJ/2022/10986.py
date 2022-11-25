import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
sum = [0]*n
cnt = [0]*m # m으로 나눠떨어지는 수니까 0~m-1까지임
sum[0] = arr[0]
answer=0
# 합배열
for i in range(1,n):
    sum[i] = sum[i-1] + arr[i]
for i in range(n):
    if sum[i]%m==0:
        answer+=1
    cnt[sum[i]%m]+=1

for i in range(m):
    if cnt[i]>1:
        answer+=(cnt[i]*(cnt[i]-1)//2)
print(answer)
