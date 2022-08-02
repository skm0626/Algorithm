from collections import deque

dq=deque()
answer=0
tmp=1

n = list(input())
for i in range(len(n)):
    if n[i]=="(":
      dq.append(n[i])
      tmp*=2
    elif n[i]=="[":
      dq.append(n[i])
      tmp*=3
    elif n[i] == ")":
        if not dq or dq[-1]=="[": #처음에 )가 들어오면 x
            answer=0
            break
        if n[i-1]=="(":
            answer+=tmp
        dq.pop()
        tmp//=2
    else:
        if not dq or dq[-1]=="(":
            answer=0
            break
        if n[i-1]=="[":
            answer+=tmp
        dq.pop()
        tmp//=3
if dq:
    print("0")
else:
    print(answer)