from itertools import combinations

# C2
def make_candidate(freq_itemsets,k): #k=몇개짜리 만드는지
    candidates = set()
    for itemset1 in freq_itemsets:
        for itemset2 in freq_itemsets:
            union = itemset1.union(itemset2) # itemset1 | itemset2
            if len(union) == k:
                for item in union: # {a b}, {b c}, {c d} => {a b c} 가 나오는데 {a c}는 없으니까 얜 freq가 될 수 없음 -> {a b c}는 있으면 안됨
                    if union-{item} not in freq_itemsets:
                        break
                else:  # for문의 else = break에서 걸리면 else안들어옴
                    candidates.add(union)
    return candidates

def filter(candidates,k,s):
    itemsets_cnt_k = {}
    with open("groceries.csv","r") as f:
        for line in f:
            basket = line.strip().split(",")
            for comb in combinations(basket,k):
                comb = frozenset(comb)
                if comb in candidates:
                    if comb not in itemsets_cnt_k:
                        itemsets_cnt_k[comb]=0
                    itemsets_cnt_k[comb]+=1
    # print(itemsets_cnt_2)
    freq_itemsets=set(itemset for itemset,cnt in itemsets_cnt_k.items() if cnt>=s) #set에는 set이 안들어가서 frozenset으로하면 들어가짐
    return freq_itemsets

# item 개수 구하기
s=100

item_cnt={}

with open("groceries.csv","r") as f:
    for line in f:
        # print(line)
        # print(line.strip().split(",")) # 하나의 리스트가 basket
        basket = line.strip().split(",")
        for item in basket:
            if item not in item_cnt:
                item_cnt[item]=0
            item_cnt[item]+=1
# print(item_cnt)

#frequent한 애들만 남기기
# frep_items=set()
# for item,cnt in item_cnt.items():
#     if cnt >= s:
#         freq_items.add(item)

# L1  ppt에서 7페이지 그림
freq_itemsets=set(frozenset([item]) for item,cnt in item_cnt.items() if cnt>=s) #set에는 set이 안들어가서 frozenset으로하면 들어가짐
# print(freq_items)
freq_itemsets_all = freq_itemsets.copy()

k=2
while len(freq_itemsets)>0:
    candidates = make_candidate(freq_itemsets,k)
    freq_itemsets = filter(candidates,k,s)
    freq_itemsets_all |= freq_itemsets
    print(k, len(candidates), len(freq_itemsets))
    k+=1

for fi in freq_itemsets_all:
    print(fi)