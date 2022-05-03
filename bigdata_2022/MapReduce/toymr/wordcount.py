from emit import *

def map_func(key, value):
    # code here!
    for w in value.split():
        emit(w,1)
    

def reduce_func(key, values):
    # code here!
    emit(key,sum(values))

# 진짜 단어들이 몇개 들어있는지  (distinct한 것들 말고!)
# def map_func(key, value):
#     # code here!
#     for w in value.split():
#         emit("words",1)
    

# def reduce_func(key, values):
#     # code here!
#     emit(key,sum(values))

# 사실 그냥 wc -l output.txt하면 다 세줌!