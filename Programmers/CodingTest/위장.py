import itertools
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]]+=1
        else:
            dic[i[1]]=1
    # print(dic)
    # print(list(dic.values())[0])
    for i in range (len(dic)):
        # 상의가 2가지 인 경우 - 아무것도 안입기, 상의1, 상의2 -> 3가지 경우
        answer = answer * (list(dic.values())[i]+1)
    return answer-1 # 아무것도 안입는 경우 빼기
