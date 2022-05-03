from emit import *

# distinct한 단어가 총 몇개있는지 구하기 = mapreduce 두번 돌리면 됨
# 실행법
# python toymr.py wordcount littleprince.txt  output.txt
# python toymr.py wordcount_step2 output.txt real_output.txt
# def map_func(key, value):
#     emit("distinct_words",1)
    

# def reduce_func(key, values):
#     emit(key,sum(values))

# 각 distinct한 단어들마다 단어가 몇번 등장했는지를  셌음
# 이 숫자들을 제곱해서 합하기
# python toymr.py wordcount littleprince.txt  output.txt
def map_func(key, value):
    v = int(value.split()[1])**2
    emit("distinct_words",v)
    

def reduce_func(key, values):
    emit(key,sum(values))
