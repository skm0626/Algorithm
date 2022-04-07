# 터미널 창에서 python bloomfilter.py 로 실행
import math
import mmh3
import random

class BloomFilter:
    def __init__(self, capacity, fp_prob): #capacity = 집합 S의 최대 크기(ppt에서 m), falsepositive비율
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.bitarray = 0
        self.n_bits = math.ceil(-math.log(fp_prob,math.e)*capacity/(math.log(2,math.e)**2)) #피피티 p.17
        self.n_hashs = int(self.n_bits/capacity * math.log(2,math.e)) #해시 함수 개수 ppt p.17
        self.seeds = [random.randint(0,999999) for i in range(self.n_hashs)]

    def put(self, item):
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits
            self.bitarray |= (1<<pos)

    def test(self, item):
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits

            if self.bitarray & (1<<pos) == 0:
                return False
        return True

bloom = BloomFilter(5,0.1)
bloom.put('a')
bloom.put('b')
bloom.put('c')
bloom.put('d')
bloom.put('e')

print('a',bloom.test('a'))
print('b',bloom.test('b'))
print('c',bloom.test('c'))
print('d',bloom.test('d'))
print('e',bloom.test('e'))
print('f',bloom.test('f'))
print('g',bloom.test('g'))
print('h',bloom.test('h'))
print('i',bloom.test('i'))