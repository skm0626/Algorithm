from bisect import bisect_left, bisect_right

x = int(input())
arr = list(map(int,input().split()))

a = bisect_left(arr,x)
b = bisect_right(arr,x)
print(b-a)
