import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())

def isPrime(x):
    for i in range(2,int(x/2)+1):
        if x%i == 0:
            return False
    return True

def DFS(y):
    if len(str(y)) == n:
        print(y)
    else:
        for i in range(1,10):
            if i%2==0:
                continue
            if isPrime(y*10+i):
                DFS(y*10+i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
