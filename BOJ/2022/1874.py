import sys
n = int(sys.stdin.readline())
arr = []
num = 1
st = []
answer = ''

for i in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)

for i in range(n):
    su = arr[i]
    if su>=num:
        while su>=num:
            st.append(num)
            num+=1
            answer+="+\n"
        st.pop()
        answer+="-\n"
    else:
        k = st.pop()
        if k>su:
            answer = "NO"
            break
        else:
            answer+="-\n"

print(answer)
