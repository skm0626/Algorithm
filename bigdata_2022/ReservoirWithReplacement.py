import random
import matplotlib.pyplot as plt

class Reservoir:
    def __init__(self,k): #k개 샘플링하겠다.
        self.sampled = []
        self.k = k
        self.cnt =0 # 몇 번째로 들어온 아이템인지

    def put(self, item): #스트림에서 item 하나가 reservoir sampled로 들어옴
        if self.cnt < self.k: # k개 이하로 들어올 경우 : 배열에 그냥 추가
            self.sampled.append(item)
        else: # k개 이상이 들어왔을 경우 : r<k일 때만 r번재 값을 item으로 대체
            r = random.randint(0,self.cnt)
            # randint randrange 차이
            # randint(0,10) : 0~10 # randrange(0,10) : 0~9
            if r<self.k:
                self.sampled[r] = item
        self.cnt += 1

cnt = [0 for i in range(1000)]

for i in range(10000): #10000
    reservoir = Reservoir(100)
    for j in range(1000):
        reservoir.put(j)
        print(reservoir.sampled)
        if j in reservoir.sampled:
            cnt[j]+=1


# 시각화
x = [i for i in range(1000)]
y = cnt
plt.bar(x,y,width=1)
# plt.set_ylim([0,10000])
# plt.set(title='Count' ,xlabel='숫자',ylabel='추출횟수')
plt.show()
