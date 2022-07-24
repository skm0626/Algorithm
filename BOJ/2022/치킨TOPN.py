n = int(input())
array = list(map(int, input().split()))
k = int(input())

index = n // k
arr = []

for i in range(0,n,index):
    arr+=sorted(array[i:i+index])
print(" ".join(str(i) for i in arr))