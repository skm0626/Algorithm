n,m = map(int,input().split())
arr = list(map(int,input().split()))

start=0
end=max(arr)-1

answer=0
while (start<=end):
    len = 0
    mid = (start+end)//2
    for i in range(n):
        if arr[i]>mid:
            len += arr[i]-mid
    if len<m:
        end = mid-1
    else:
        answer=mid
        start = mid+1
print(answer)
