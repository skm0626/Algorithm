n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(str, input().split())))
# 1순위 인것을 가장 마지막에 해야 1순위로 적용됨
arr.sort(key=lambda x:str(x[0]))
arr.sort(key=lambda x:int(x[3]), reverse=True)
arr.sort(key = lambda x:int(x[2]))
arr.sort(key = lambda x:int(x[1]), reverse = True)

for i in range(len(arr)):
    print(arr[i][0])