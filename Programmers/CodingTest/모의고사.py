import math
import numpy as np
def solution(answers):
    answer = []
    arr=[]
    score = [0,0,0]
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one = one*math.ceil(len(answers)/len(one))
    one = one[:len(answers)]
    two = two*math.ceil(len(answers)/len(two))
    two = two[:len(answers)]
    three = three*math.ceil(len(answers)/len(three))
    three = three[:len(answers)]
    # print(two)
    for idx, ans in enumerate(answers):
        if one[idx] == ans:
            score[0]+=1
        if two[idx] == ans:
            score[1]+=1
        if three[idx] == ans:
            score[2]+=1
    m = max(score)
    for idx, s in enumerate(score):
        if s == m:
            answer.append(idx+1)
    return answer
