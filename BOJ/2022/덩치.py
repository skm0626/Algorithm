import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in arr:
    k=1
    for j in arr:
        if (i[0]<j[0] and i[1]<j[1]):
            k+=1
    print(k,end=' ')