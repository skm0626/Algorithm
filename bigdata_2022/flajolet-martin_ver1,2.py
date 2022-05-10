import mmh3
import math
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

class FM1:
    def __init__(self, domain_size): #들어오는 item이 어느 배열에서 들어오는지 그 배열의 크기
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
        arr.append(r)

    def size(self): # 개수 세기
        R = max(arr)
        return 2**R


class FM2:
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

arr = []

fm1 = FM1(1000000) # 예측한 것
tset1 = set() #true set 실제로 집합에 넣은것
fm2 = FM2(1000000) # 예측한 것
tset2 = set() #true set 실제로 집합에 넣은것
x1=[]
y1=[]
x2=[]
y2=[]
for i in tqdm(range(10000)):
    item = str(random.randint(0,100000))
    fm1.put(item)
    tset1.add(item)
    fm2.put(item)
    tset2.add(item)

    x1.append(len(tset1))
    y1.append(fm1.size())
    x2.append(len(tset2))
    y2.append(fm2.size())

plt.scatter(x1,y1)
plt.plot(x1,x1,color='g') # y=x축 그려보기
plt.scatter(x2,y2,color='r')
plt.show()