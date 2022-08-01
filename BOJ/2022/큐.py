from collections import deque
import sys

dq = deque()
def push(x):
    dq.append(x)
def pop():
    if len(dq)!=0:
        print(dq.popleft())
    else:
        print("-1")
def size():
    print(len(dq))
def empty():
    if (len(dq)!=0):
        print("0")
    else:
        print("1")
def front():
    if (len(dq)!=0):
        print(dq[0])
    else:
        print("-1")
def back():
    if (len(dq)!=0):
        print(dq[-1])
    else:
        print("-1")

n = int(sys.stdin.readline())
for i in range(n):
    m = sys.stdin.readline()
    if "push" in m:
        h = m.split()
        push(h[1])
    elif "pop" in m:
        pop()
    elif "size" in m:
        size()
    elif "empty" in m:
        empty()
    elif "front" in m:
        front()
    elif "back" in m:
        back()