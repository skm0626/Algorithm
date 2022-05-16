n = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=True)

answer = 0
temp = 0
for i in arr:
    temp+=1
    if temp>=i:
        answer +=1
        temp=0
print(answer)
