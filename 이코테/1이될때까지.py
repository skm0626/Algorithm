n, k = map(int,input().split())
answer=0
# while n>1:
#     if n%k==0:
#         n = n//k
#         answer += 1
#     else:
#         n-=1
#         answer += 1
#
# print(answer)
# 이 방법은 돌리면서 1씩 빼서 비효율적임

while True:
    target = (n//k)*k
    answer += n-target
    n = target

    if n<k:
        break

    n = n//k
    answer+=1

answer += (n-1)
print(answer)
