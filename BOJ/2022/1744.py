n = int(input())
plus = []
minus = []
result = 0

for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

plus.sort(reverse=True)
minus.sort()

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)


####################################################################################
########################DO IT!코테 책대로 하면 시간초과남##############################
# import sys
# from queue import PriorityQueue
# n = int(sys.stdin.readline())
# pluspq = PriorityQueue()
# minuspq = PriorityQueue()
# one=0
# zero=0
# sum=0

# for i in range(n):
#     m = int(sys.stdin.readline())
#     if m>1:
#         pluspq.put(m*(-1)) # 큰수부터 정렬하려고 -1 곱합
#     elif m<0:
#         minuspq.put(m)
#     elif m==1:
#         one+=1
#     elif m==0:
#         zero+=1

# while pluspq.qsize()>1:
#     x = pluspq.get() *-1
#     y = pluspq.get() *-1
#     sum+=x*y

# if pluspq.qsize()==1:
#     sum+=pluspq.get() *-1

# while minuspq.qsize()>1:
#     x = pluspq.get()
#     y = pluspq.get()
#     sum += x * y

# if minuspq.qsize()==1:
#     if zero==0:
#         sum+=minuspq.get()

# sum+=one
# print(sum)
