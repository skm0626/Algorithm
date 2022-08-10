import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque(enumerate((map(int,sys.stdin.readline().split()))))
answer = []
num=0
start=0

while dq:
    idx, num=dq.popleft()
    answer.append(idx+1)
    if num>0:
        dq.rotate(-num+1)
    else:
        dq.rotate(-num) # num으로 하면 안됨?!?!?!?
print(' '.join(map(str,answer)))

