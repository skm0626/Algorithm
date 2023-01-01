import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            tmp = arr[j+1]
            arr[j+1]=arr[j]
            arr[j]= tmp
for i in arr:
    print(i)