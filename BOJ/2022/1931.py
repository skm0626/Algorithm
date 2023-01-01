import sys
n = int(sys.stdin.readline())
arr = []
answer=0

for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([b,a])

arr.sort()
end = -1

for i in range(len(arr)):
    if arr[i][1]>=end:
        answer+=1
        end = arr[i][0]
print(answer)