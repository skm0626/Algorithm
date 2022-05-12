import math
def solution(progresses, speeds):
    answer = []
    end = []
    for i in range (len(progresses)):
        n = math.ceil((100-progresses[i])/speeds[i])
        end.append(n)
    # print(end)
    idx=0
    for i in range (len(end)):
        if end[idx]<end[i]:
            answer.append(i-idx)
            idx=i
    answer.append(len(end)-idx)
    return answer
