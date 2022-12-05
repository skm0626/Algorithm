import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    arr.append([x,y])
arr.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(arr[i][0],arr[i][1])
