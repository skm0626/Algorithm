def solution(genres, plays):
    answer = []
    total = {}
    dic = {} # 장르별 정보[재생횟수, 인덱스]
    for i in range (len(genres)):
        if genres[i] in total:
            total[genres[i]]+=plays[i]
            dic[genres[i]].append([plays[i],i])
        else:
            total[genres[i]]=plays[i]
            dic[genres[i]]=[[plays[i],i]]
    # print(total)
    # 가장 많이 재생된 장르별로 정렬
    total = sorted(total.items(), key = lambda x:x[1],reverse = True) #total.items()로 정렬해야 모든 원소가 포함되어 정렬됨(total만 했더니 total에 키만 남아있음)
    # print(total)
    for g in total:
        print(g)
        arr = dic[g[0]] # arr = 장르별 재생횟수랑 인덱스
        # print(arr)
        arr = sorted(arr,key=lambda x:x[0],reverse=True)
        for i in range(len(arr)):
            if i<2:
                answer.append(arr[i][1])
    return answer
