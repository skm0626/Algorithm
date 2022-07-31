# 백준
# 방법 1
# python3로 하면 시간초과
# pypy3로 하면 성공
# from sys import stdin
# n = int(stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
# for i in range(len(arr)):
#     print(arr[i])

# 방법 2
# input, output을 다르게 하면 빠르게 됨
# python3로 해도 성공
# from sys import stdin
# import sys
# n = int(stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# arr.sort()
# for i in (arr):
#     sys.stdout.write(str(i)+'\n')

# 위의 방법은 퀵정렬로 최악의 경우 시간복잡도가 O(n^2)임
# 따라서 병합정렬로 구현해보기
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
