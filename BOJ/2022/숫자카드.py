import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))
dict = dict()
for i in arr:
    dict[i]=1
# print(dict)
for i in arr2:
    if dict.get(i)==1:
        print(1, end=' ')
    else:
        print(0, end=' ')