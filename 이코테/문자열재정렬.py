n = input()
s=[]
num=0
answer = ''
for i in n:
    if i.isalpha(): # ord(i)>=65:
        s.append(i)
    else:
        num+=int(i)
s.sort()
for i in s:
    answer += i
answer+=str(num)
print(answer)
