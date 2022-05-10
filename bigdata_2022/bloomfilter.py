# 터미널 창에서 python bloomfilter.py 로 실행
import math
import mmh3 # murmurhash (해쉬함수임)
import random
import string

class BloomFilter:
    def __init__(self, capacity, fp_prob): #capacity = 집합 S의 최대 크기(ppt에서 m), falsepositive비율(얼마까지 허용할지)
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.bitarray = 0 # bit배열
        self.n_bits = math.ceil(-math.log(fp_prob,math.e)*capacity/(math.log(2,math.e)**2)) # bit배열의 사이즈 (ppt에서 n, p.16참고)
        self.n_hashs = int(self.n_bits/capacity * math.log(2,math.e)) #해시 함수 개수(ppt에서 최적의 k, p.17참고)
        self.seeds = [random.randint(0,999999) for i in range(self.n_hashs)]

    def put(self, item):
        real_data.append(item)
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits # seeds를 주면 item이 같아도 seed에 따라 다른 결과값이 나옴!
            # self.n_bits로 나누는 이유 : bit배열의 어느 위치에 넣을지 정하기 위해
            self.bitarray |= (1<<pos) # set하기

    def test(self, item): # 있는지 없는지
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits
            # 해당 pos가 전부 1이면 있을 수 있다!
            if self.bitarray & (1<<pos) == 0:
                return False
        return True

real_data = []
test_data = []
false_positive = 0.1
fp=0
arr_str=set()

bloom = BloomFilter(5, false_positive)
bloom.put('a')
bloom.put('b')
bloom.put('c')
bloom.put('d')
bloom.put('e')
# print(random.choice(string.ascii_lowercase))
for i in range(30):
    str = random.choice(string.ascii_lowercase)
    arr_str.add(str)
arr_str = list(arr_str)
# print(arr_str)
for i in range(len(arr_str)):
    # print(arr_str[i], bloom.test(arr_str[i]))
    test_data.append(arr_str[i])
# print('a',bloom.test('a'))
# print('b',bloom.test('b'))
# print('c',bloom.test('c'))
# print('d',bloom.test('d'))
# print('e',bloom.test('e'))
# print('f',bloom.test('f'))
# print('g',bloom.test('g'))
# print('h',bloom.test('h'))
# print('i',bloom.test('i'))

# 확인하기
for i in range(len(test_data)):
    if (test_data[i] not in real_data and bloom.test(test_data[i])==True):
        fp+=1
print("real data : ", real_data)
print("test data : ", test_data)
print("설정한 false positive : ", false_positive)
print("테스트 결과의 false positive rate : ",fp/len(test_data))