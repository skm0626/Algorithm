import sys

n,k = map(int,sys.stdin.readline().split())
arr = [0]*1000001
min_idx=sys.maxsize
max_idx=0
ans=0
ice=0

for i in range(n):
    g,x = map(int, sys.stdin.readline().split())
    arr[x]=g
    min_idx = min(min_idx,x)
    max_idx = max(max_idx,x)
end = min_idx
for start in range(min_idx,max_idx+1):
    while end<=max_idx and end-start<=k*2:
    # 특정 좌표 x 에서 x - k 부터 x + k 까지의 범위를 확인해야 하므로 end 와 start 차이가 K * 2 이하일때까지 end를 증가
        # if arr[end]==0:
        #     end+=1
        #     continue
        ice += arr[end]
        end+=1
    ans = max(ans,ice)
    ice -= arr[start]
print(ans)
