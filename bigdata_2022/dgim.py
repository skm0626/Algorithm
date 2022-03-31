import random
class Bucket:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self):
        return f"({self.start}, {self.end})"

class DGIM:
    # 원래는 체크할 max size가 있는데 무한대로 하겠음
    # [시작 timestamp, 끝 timestamp, 길이] 인데 길이는 생략하겠음
    def __init__(self):
        self.bucket_tower = [[]]
        self.ts = 0 #timestamp

    def put(self, bit):
        if bit==1:
            b = Bucket(self.ts, self.ts)
            self.bucket_tower[0].insert(0,b)

            layer = 0
            while len(self.bucket_tower[layer]) > 2:
                if len(self.bucket_tower) <= layer+1:
                    self.bucket_tower.append([])

                b1 = self.bucket_tower[layer].pop()
                b2 = self.bucket_tower[layer].pop()
                b1.end = b2.end

                self.bucket_tower[layer+1].insert(0,b1)
                layer += 1
        self.ts += 1

            # s 가 버킷 사이에 있을 수도 있음!
# 0010110[10111]0[101][1]0[1]
        # s   e
    def count(self,k): #추론!
        s = self.ts - k #start
        cnt = 0
        for layer, buckets in enumerate(self.bucket_tower):
            for bucket in buckets:
                if s <= bucket.start:
                    cnt += (1<< layer) # = 2 ** layer
                elif s <= bucket.end: # 위 주석의 예시
                    cnt += (1<<layer) * (bucket.end- s + 1) // (bucket.end - bucket.start + 1)
                    return cnt
                else:
                    return cnt
        return cnt

dgim = DGIM()
# for _ in range(20):
#     dgim.put(1)
#     print(dgim.bucket_tower)

# for b in [0,1,0,1,1,0,1,1,1,1,1,0,0,0,1]:
#     dgim.put(b)
#     print(dgim.bucket_tower)
#
# for k in range (1,10):
#     print(k, dgim.count(k))

#실제 1의 값이랑 dgim으로 구한 값이랑 얼마나 차이나는지 확인!
bitstream = []
for i in range (10):
    prob = random.random() #1일 확률(prob = 0~1사이값)
    for j in range(random.randint(20,50)):
        if random.random() <prob:
            bitstream.append(1)
        else:
            bitstream.append(0)
for b in bitstream:
    dgim.put(b)
for k in range (1,200):
    print(k, dgim.count(k), sum(bitstream[-k:])) # 앞은 예측값, 뒤는 실제값
