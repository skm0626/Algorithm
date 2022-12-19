import sys
n,m = map(int,sys.stdin.readline().split())
dna = list(sys.stdin.readline())
checkList = list(map(int,sys.stdin.readline().split()))
answer = 0

nowList = [0] * 4
checkSecret = 0 #몇 개의 문자가 충족됐는지 판단하는 변수

def add(x):
    global checkSecret, nowList, checkList
    if x=='A':
        nowList[0]+=1
        if nowList[0] == checkList[0]:
            checkSecret+=1
    elif x=='C':
        nowList[1]+=1
        if nowList[1] == checkList[1]:
            checkSecret+=1
    elif x=='G':
        nowList[2]+=1
        if nowList[2] == checkList[2]:
            checkSecret+=1
    elif x=='T':
        nowList[3]+=1
        if nowList[3] == checkList[3]:
            checkSecret+=1

def remove(x):
    global checkSecret, nowList, checkList
    if x == 'A':
        if nowList[0] == checkList[0]:
            checkSecret-=1
        nowList[0]-=1
    elif x == 'C':
        if nowList[1] == checkList[1]:
            checkSecret-=1
        nowList[1]-=1
    elif x == 'G':
        if nowList[2] == checkList[2]:
            checkSecret-=1
        nowList[2]-=1
    elif x == 'T':
        if nowList[3] == checkList[3]:
            checkSecret-=1
        nowList[3]-=1

for i in range(4):
    if checkList[i]==0: #0개이면 무족한 만족한 것임
        checkSecret+=1
for i in range(m): #초기 m부분 문자열 처리
    add(dna[i])

if checkSecret==4:
    answer+=1

for i in range(m,n):
    j = i-m
    add(dna[i])
    remove(dna[j])
    if checkSecret==4:
        answer+=1
print(answer)
