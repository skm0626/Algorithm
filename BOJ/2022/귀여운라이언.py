import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
end=0
lion=0
answer=int(1e9)

if arr.count(1)<k:
    print("-1")
    exit()

for start in range(n):
    while lion<k and end<n:
        if arr[end]==1:
            lion+=1
        end+=1
    if lion==k:
        answer = min(end-start,answer)
        if arr[start]==1:
            lion-=1
print(answer)