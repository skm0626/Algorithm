def solution(genres, plays):
    answer = []
    total = {}
    dic = {} # 장르별
    for i in range (len(genres)):
        if genres[i] in total:
            total[genres[i]]+=plays[i]
            dic[genres[i]].append([plays[i],i])
        else:
            total[genres[i]]=plays[i]
            dic[genres[i]]=[[plays[i],i]]
    # print(total)
    total = sorted(total.items(), key = lambda x:x[1],reverse = True) #total.items()로 정렬해야 모든 원소가 포함되어 정렬됨(total만 했더니 total에 키만 남아있음)
    # print(total)
    for g in total:
        print(g)
        arr = dic[g[0]]
        print(arr)
    # return answer
