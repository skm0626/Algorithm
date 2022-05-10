import mmh3
import math
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import statistics

class FM:
    def __init__(self, domain_size): #들어오는 item이 어느 배열에서 들어오는지 그 배열의 크기
        self.bitarray = 0
        self.domain_size = domain_size
        self.n_bits = math.ceil(math.log2(domain_size)) #몇개 비트 쓸건지 #int로 표현하려고 ceil
        self.mask = (1<<self.n_bits)-1 # 아래 put함수에서 hash함수를 통해 나온 값중에 n_bits(개수)만큼만 사용할거니까 필요없는 부분 삭제하기 위해 mask
        self.seed = random.randint(0,9999999) # hash를 여러개 쓸 수도 있으니까

    def put(self,item):
        h = mmh3.hash(item, self.seed) & self.mask
        r = 0 # least significant set bit
        if h==0: return
        while (h&(1<<r)==0):
            r+=1
        self.bitarray |= (1<<r) #r번 위치에 1세팅

    def size(self): # 개수 세기
        R=0
        while (self.bitarray & (1<<R) != 0): # 0이 처음 나온 위치
            R+=1
        return 2**R / 0.77351

n_hash = 100 # hash fuction 개수
group = 100 # group개수
X = []
Y = []
group_mean_x=[0 for i in range(group)]
group_mean_y=[0 for i in range(group)]

for j in range(n_hash):
    fm = FM(1000000) # 예측한 것
    tset = set() #true set 실제로 집합에 넣은것

    x=[]
    y=[]

    for i in tqdm(range(10000)):
        item = str(random.randint(0,100000))
        fm.put(item)
        tset.add(item)

        x.append(len(tset))
        y.append(fm.size())
    X.append(x)
    Y.append(y)
    print(len(X))
group_arr_x = [X[i:i+n_hash//group] for i in range(0,len(X),n_hash//group)] # 그룹별로 배열 나누기
group_arr_y = [Y[i:i+n_hash//group] for i in range(0,len(Y),n_hash//group)]
# print(len(group_arr_x))
# print(np.average(group_arr_x[0],axis=0))

for i in range(group): # 각 그룹별로 중앙값 구하기
    group_mean_x[i] = np.median(group_arr_x[i],axis=0)
    group_mean_y[i] = np.median(group_arr_y[i], axis=0)
# print(len(group_mean_x))
# 총 평균 구하기
total_mean_x = np.average(group_mean_x,axis=0)
total_mean_y = np.average(group_mean_y,axis=0)
# print(len(total_mean_x))
plt.scatter(total_mean_x,total_mean_y)
plt.plot(x,x,color='r') # y=x축 그려보기
plt.show()

