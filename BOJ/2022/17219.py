import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = {}

for _ in range(N):
    site, ps = input().split()
    s[site] = ps

for _ in range(M):
    print(s[input().rstrip()])
