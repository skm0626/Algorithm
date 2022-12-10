import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
ans = 0
start = 0
end = n-1

while start<end:
    if arr[start]+arr[end]<m:
        start+=1
    elif arr[start]+arr[end]>m:
        end-=1
    else:
        ans+=1
        start+=1
        end-=1
print(ans)