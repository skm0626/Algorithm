import sys
import math

a,b,v = map(int,sys.stdin.readline().split())
answer = (v-b)/(a-b)
print(math.ceil(answer))
