import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
answer=0

for i in range(n):
    target = arr[i]
    start = 0
    end = n-1
    while start<end:
        if arr[start]+arr[end]<target:
            start+=1
        elif arr[start]+arr[end]>target:
            end-=1
        else:
            if start!=i and end!=i:
                answer+=1
                break
            elif start==i:
                start+=1
            else:
                end-=1
print(answer)
