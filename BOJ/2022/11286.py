from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    m = int(input())
    if m == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        myQueue.put((abs(m),m))
        
################### print와 print = sys.stdout.write의 차이 ########################
################### print는 저절로 뒤에 '\n'이 붙음 / sys.stdout.write을 사용하려면 직접 위의 코드 처럼 '\n'을 추가해야함
        
import sys
from queue import PriorityQueue
# print = sys.stdout.write
n = int(sys.stdin.readline())
myQueue = PriorityQueue()
for i in range(n):
    m = int(sys.stdin.readline())
    if m==0:
        if myQueue.empty():
            print('0')
        else:
            tmp = myQueue.get()
            print(str(tmp[1]))
    else:
        myQueue.put((abs(m), m))
