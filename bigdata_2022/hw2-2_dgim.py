import random
import matplotlib.pyplot as plt

class Bucket:
    def __init__(self, start, end, num):
        self.start = start
        self.end = end
        self.num=num # 버킷의 합을 저장할 변수
    def __repr__(self): # 버킷을 출력해보기 위해
        return f"({self.start}, {self.end}, {self.num})"

class DGIM:
    def __init__(self):
        self.bucket_tower = [[]]
        self.ts = 0 #timestamp

    def put(self, n):
        b = Bucket(self.ts, self.ts, n)
        self.bucket_tower[0].insert(0,b)

        layer = 0
        while len(self.bucket_tower[layer]) > 2: # 2개 초과 즉, 3개 이상이면 그중 2개 합쳐서 위 layer로
            if len(self.bucket_tower) <= layer+1: # 다음 layer가 있는지 확인 -> 없으면 추가
                self.bucket_tower.append([])
            if (self.bucket_tower[layer][-1].num + self.bucket_tower[layer][-2].num <= 2**(layer+1)): # 해당 layer의 뒤에 두개의 합이 바로 위 영역(layer+1)의 크기보다 작을 경우 -> 2개를 합해서 올리기
                b1 = self.bucket_tower[layer].pop()
                b2 = self.bucket_tower[layer].pop()
                b1.end = b2.end
                b1.num+=b2.num # 두 수를 합해서 넣어주기
                self.bucket_tower[layer+1].insert(0,b1)
            else: # 한 개만 위 영역으로 올리기
                b1 = self.bucket_tower[layer].pop()
                self.bucket_tower[layer + 1].insert(0, b1)
            layer += 1
        self.ts += 1

    def count(self,k): #추론!
        s = self.ts - k #start
        cnt = 0 # 총 합을 나타내는 변수
        for layer, buckets in enumerate(self.bucket_tower):
            for bucket in buckets:
                if s <= bucket.start: # 완전히 포함된 것
                    cnt += bucket.num # 영역 합 모두 합하기
                elif s <= bucket.end: # 걸쳐있는 경우
                    cnt += bucket.num * (bucket.end- s + 1) // (bucket.end - bucket.start + 1) # 몇개 걸쳐져 있는지=bucket.end- s + 1 # 전체 사이즈=bucket.end - bucket.start + 1
                    return cnt
                else:
                    return cnt
        return cnt

stream = []
real=[]
for i in range (10000):
    j=random.randint(0,15)
    real.append(j)
    stream.append(j)
print("stream : ", stream)

dgim = DGIM()
dgim_result=[0 for i in range(2001)]
real_result=[0 for i in range(2001)]

for b in stream:
    dgim.put(b)
    # print(dgim.bucket_tower)
for k in range (1,2001):
    dgim_result[k]=dgim.count(k)
    real_result[k]=sum(stream[-k:]) # 앞은 예측값, 뒤는 실제값

print(real_result[-1], sum(real[-2000:]), dgim_result[-1])

# 시각화
plt.subplot(311)
plt.plot([i for i in range(2001)], real_result)
plt.subplot(312)
plt.plot([i for i in range(2001)], dgim_result,'r-')
plt.subplot(313)
plt.plot([i for i in range(2001)], real_result, [i for i in range(2001)], dgim_result,'r-')
plt.show()