n = int(input())
answer=0
coin = [500,100,50,10]

for c in coin:
    answer += n//c
    n = n%c

print(answer)
