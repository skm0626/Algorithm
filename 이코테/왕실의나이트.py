n = str(input())
answer=0

x = int(ord(n[0]) - ord('a')) + 1 #체스판이 1부터 시작하니까(a가 입력되었다면 a-a=0이 되니까 1을 더해줘야함)
y = int(n[1])

dic = [[2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,1],[-1,2],[-1,-2]]

for i in dic:
    nx = x + i[0]
    ny = y + i[1]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    else:
        answer+=1
print(answer)
