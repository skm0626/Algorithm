def solution(participant, completion):
    # 이게 더 깔끔한 풀이!
    # import collections     
    # answer = collections.Counter(participant) - collections.Counter(completion)
    # return list(answer.keys())[0]
    dic = {}
    for i in participant:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in completion:
        if dic[i]==1:
            del dic[i]
        else:
            dic[i]-=1
    return list(dic.keys())[0]
