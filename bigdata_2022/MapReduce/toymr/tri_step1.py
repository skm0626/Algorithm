from emit import *

def map_func(key,value):
    u, v = map(int,value.split())
    emit(u,v)

def reduce_func(key, values):
    for u in values:
        for v in values:
            if u<v:
                emit(f"{u}\t{v}",key)