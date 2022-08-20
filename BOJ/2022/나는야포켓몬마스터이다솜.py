import sys
n,m = map(int,sys.stdin.readline().split())
dict = dict()
for i in range(n):
    k = sys.stdin.readline().rstrip()
    dict[k] = i+1
    dict[i+1]=k
for j in range(m):
    h = sys.stdin.readline().rstrip()
    if h.isdigit():
       print(dict[int(h)])
    else:
        print(dict[h])
