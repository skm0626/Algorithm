import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    func = sys.stdin.readline()
    n = int(sys.stdin.readline())
    dq = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    flag=0

    if n == 0:
        dq = []

    for k in func:
        if k=='R':
            flag+=1
            # dq.reverse()
        elif k=='D':
            if len(dq)==0:
                print("error")
                break
            else:
                if flag%2==0:
                    dq.popleft()
                else:
                    dq.pop()
    # if len(dq):
    else:
        if flag%2==0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")
    # else:
    #     print("error")
    # 테스트케이스
    # 1 R 0 []
    # 인 경우엔 내가 처음에 시도했던 대로 아래서 if len(dq) 조건문으로 error를 출력하면
    # 에러가 되어버림
    # 하지만 R일 때 에러를 출력하라는 조건은 없음!
    # 빈 배열이더라도 R이면 빈배열 출력해야함