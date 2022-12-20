import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
ans = [0]*n
st = []
result=""

for i in range(n):
    while st and arr[st[-1]]<arr[i]:
        ans[st.pop()] = arr[i]
    st.append(i)

while st:
    ans[st.pop()] = -1

print(*ans)
