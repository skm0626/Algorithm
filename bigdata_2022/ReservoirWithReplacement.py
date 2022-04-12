import random
class Reservoir:
    def __init__(self,k): #k개 샘플링하겠다.
        self.sampled = []
        self.k = k
        self.cnt =0 # 몇 번째로 들어온 아이템인지

    def put(self, item): #스트림에서 item 하나가 reservoir sampled로 들어옴
        if self.cnt < self.k:
            self.sampled.append(item)
        else:
            r = random.choice(self.cnt+1,1,replace=True)
            # randint randrange 차이
            # randint(0,10) : 0~10 # randrange(0,10) : 0~9
            if r<self.k:
                self.sampled[r] = item
        self.cnt += 1

reservoir = Reservoir(20)

for i in range(1000):
    reservoir.put(i)
    print(reservoir.sampled)
