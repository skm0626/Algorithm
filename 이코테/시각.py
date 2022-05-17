n = int(input())
answer=0
time=''
for i in range(n+1): # 시각은 1 더해줘야함!(입력받은 시간까지 가야하니까)
    for j in range(60):
        for k in range(60):
            time = str(i)+str(j)+str(k)
            if '3' in time:
                answer+=1
            time = ''
print(answer)
