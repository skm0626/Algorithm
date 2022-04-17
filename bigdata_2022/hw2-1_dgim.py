import random
import matplotlib.pyplot as plt

class Bucket:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self): # 버킷을 출력해보기 위해
        return f"({self.start}, {self.end})"

class DGIM:
    # 원래는 체크할 max size가 있는데 무한대로 함
    # [시작 timestamp, 끝 timestamp, 크기] 인데 크기(=1의 개수)는 생략하겠음
    def __init__(self):
        self.bucket_tower = [[]]
        self.ts = 0 #timestamp

    def put(self, bit): #bit가 아닌게 들어오는 경우는 없는 것으로 함
        if bit==1: #bit==0이면 아무 일도 할 필요 X
            b = Bucket(self.ts, self.ts)
            self.bucket_tower[0].insert(0,b) # 0번 = 1의 개수가 1개인 것 저장하는 곳! # 0번 위치에 삽입

            layer = 0
            while len(self.bucket_tower[layer]) > 2: # 2개 초과 즉, 3개 이상이면 그중 2개 합쳐서 위 layer로
                if len(self.bucket_tower) <= layer+1: # 다음 layer가 있는지 확인 -> 없으면 추가
                    self.bucket_tower.append([])
                # 3개 중 먼저 들어온 2개(= bucket_tower에서는 뒤의 2개니까 pop)를 빼기
                b1 = self.bucket_tower[layer].pop()
                b2 = self.bucket_tower[layer].pop()
                b1.end = b2.end
                self.bucket_tower[layer+1].insert(0,b1)
                layer += 1
        self.ts += 1

    def count(self,k): #추론! (k개 비트 중에서 1의 개수는?)
        s = self.ts - k #start
        cnt = 0 # 1의 개수를 나타내는 변수
        for layer, buckets in enumerate(self.bucket_tower):
            for bucket in buckets:
                if s <= bucket.start: # 완전히 포함된 것
                    cnt += (1<< layer) # = 2 ** layer
                elif s <= bucket.end: # 걸쳐있는 경우(위 주석의 예시)
                    cnt += (1<<layer) * (bucket.end- s + 1) // (bucket.end - bucket.start + 1) # 몇개 걸쳐져 있는지=bucket.end- s + 1 # 전체 사이즈=bucket.end - bucket.start + 1
                    return cnt
                else:
                    return cnt
        return cnt

bitstream = [] # 들어온 값들을 2진수로 바꾼 값을 저장할 배열
real=[] # 들어온 값들을 10진수로 그대로 저장할 배열
for i in range (10000):
    j=random.randint(0,15)
    real.append(j)
    bitstream.append(bin(j)) # 2진수로 변환하여 배열에 추가
print("bitstream : ", bitstream)

arr1=[] # 2진수의 첫번째 자리를 저장할 배열
arr2=[] # 2진수의 두번째 자리를 저장할 배열
arr3=[] # 2진수의 세번째 자리를 저장할 배열
arr4=[] # 2진수의 네번째 자리를 저장할 배열
arr=[arr4,arr3,arr2,arr1]
# 각 자리수들 별로 저장하기
for i in range(len(bitstream)):
    s = str(bitstream[i])[2:] # 이진수는 앞에 0b가 붙어있으므로 이를 제거하기 위함
    arr4.append(int(s[-1]))
    if len(s) <= 1:
        s = '000' + s
    elif len(s) <= 2:
        s = '00' + s
    elif len(s) <= 3:
        s = '0' + s
    # print("s: ",s)
    arr3.append(int(s[-2]))
    arr2.append(int(s[-3]))
    arr1.append(int(s[-4]))
# print("arr1",arr1)
# print("arr2",arr2)
# print("arr3",arr3)
# print("arr4",arr4)

dgim_result=[0 for i in range(2001)]
real_result=[0 for i in range(2001)]
for i in range(4):
    dgim = DGIM()
    for b1 in arr[i]:
        dgim.put(b1)
    for k in range(1,2001):
        dgim_result[k]+=(dgim.count(k)*(2**i))
        real_result[k]+=(sum(arr[i][-k:])*(2**i))
print(real_result[-1], sum(real[-2000:]), dgim_result[-1]) # 2진수로 변환한 것에서 구한 실제합, 10진수 수에서 구한 실제합, 첫번째 방법으로 구한 합 비교하기
# print(len(real))

# 시각화
plt.subplot(311)
plt.plot([i for i in range(2001)], real_result)
plt.subplot(312)
plt.plot([i for i in range(2001)], dgim_result,'r-')
plt.subplot(313)
plt.plot([i for i in range(2001)], real_result, [i for i in range(2001)], dgim_result,'r-')
plt.show()