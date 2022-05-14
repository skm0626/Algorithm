def solution(priorities, location):
    answer = 0
    arr = [[i,p] for i,p in enumerate(priorities)]
    while len(priorities)!=0:
        a = arr.pop(0)
        if any(a[1]<b[1] for b in arr):
            arr.append(a)
        else:
            answer+=1
            if a[0]==location:
                break
    return answer
