from emit import *

def map_func(key,value):
    tmp = value.split()
    if len(tmp) == 2: #edge
        u, v = map(int,tmp)
        emit((u,v),-1)
    else: #3 --> wedge
         u, v, w = map(int,tmp)
         emit((u,v),w)

def reduce_func(key, values):
    if -1 in values:
        for v in values:
            if v != -1:
                emit(key, v)