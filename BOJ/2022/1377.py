import sys
n = int(sys.stdin.readline())
arr = []
max = 0
for i in range(n):
    m = int(sys.stdin.readline())
    arr.append((m,i))

arr.sort()

for i in range(n):
    if max<arr[i][1]-i:
        max = arr[i][1]-i
print(max+1)
