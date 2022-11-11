import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr.sort()

for i in range(m):
    flag = False
    target = arr2[i]
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = int((start+end)/2)
        m = arr[mid]
        if target<m:
            end = mid-1
        elif m<target:
            start = mid+1
        else:
            flag = True
            break
    if flag == True:
        print(1)
    else:
        print(0)
