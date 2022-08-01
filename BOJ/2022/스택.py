import sys
n = int(sys.stdin.readline())
st = []
def push(a):
    st.append(a)
def pop():
    if (len(st)==0):
        print("-1")
    else:
        print(st.pop(-1))
def size():
    print(len(st))
def empty():
    if len(st)!=0:
        print("0")
    else:
        print("1")
def top():
    if len(st)!=0:
        print(st[-1])
    else:
        print("-1")

for i in range(n):
    x = sys.stdin.readline()
    if "push" in x:
        p = x.split()
        push(p[1])
    elif "pop" in x:
        pop()
    elif "size" in x:
        size()
    elif "empty" in x:
        empty()
    elif "top" in x:
        top()
