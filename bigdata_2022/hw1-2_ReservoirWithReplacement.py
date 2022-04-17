import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import time

class Reservoir:
    def __init__(self,k): #k개 샘플링하겠다.
        self.sampled = []
        self.k = k
        self.cnt =0 # 몇 번째로 들어온 아이템인지 나타내는 변수

    def put(self, item): #스트림에서 item 하나가 reservoir sampled로 들어옴
        if self.cnt < self.k: # k개 이하로 들어올 경우 : 배열에 그냥 추가
            self.sampled.append(item)
        else: # k개 이상이 들어왔을 경우 : r<k일 때만 r번째 값을 item으로 대체
            r = random.randint(0,self.cnt)
            if r<self.k:
                self.sampled[r] = item
        self.cnt += 1

class ReservoirWithReplacement: #복원추출을 위한 클래스
    def __init__(self,k2):
        self.k2 = k2

    def create(self,stream):
        for i in range(self.k2):
            self.reservoir = Reservoir(1) #크기 1짜리 Reservoir k번 돌리기
            for j in range(stream):
                self.reservoir.put(j)
                print(j,' : ',self.reservoir.sampled)
            arr.append(self.reservoir.sampled)

arr=[]
for i in tqdm(range(10000)):
    reservoir_replacement = ReservoirWithReplacement(100) #100개의 값을 추출
    reservoir_replacement.create(1000) #0 부터 999 까지의 숫자 입력

# 추출횟수 구하기
cnt=[0 for i in range(1000)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        cnt[arr[i][j]]+=1
print("cnt : ", cnt)

# 시각화
plt.plot([i for i in range(1000)], cnt)
plt.show()