import sys
from collections import Counter
n = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().rstrip().split()))
result=[]
ans = Counter(arr)
print(ans)
for m in arr2:
    if m in ans:
        result.append(ans[m])
    else:
        result.append(0)
print(*result)