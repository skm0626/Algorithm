n = int(input())
answer=0
for i in range(1,n+1):
    # 100미만의 수들은 무조건 한수!
    if i<100:
        answer+=1
    elif int(str(i)[1])-int(str(i)[0]) == int(str(i)[2])-int(str(i)[1]):
        answer+=1
print(answer)