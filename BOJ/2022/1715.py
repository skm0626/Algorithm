import sys
from queue import PriorityQueue
n = int(sys.stdin.readline())
pq = PriorityQueue()
sum = 0

for i in range(n):
    m = int(sys.stdin.readline())
    pq.put(m)

while pq.qsize()>1:
    x = pq.get()
    y = pq.get()
    tmp = x+y
    sum+=tmp
    pq.put(tmp)

print(sum)
