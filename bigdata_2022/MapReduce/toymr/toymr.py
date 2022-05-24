import sys
import importlib

modulename = sys.argv[1]
inputpath = sys.argv[2]
outputpath = sys.argv[3]

job = importlib.import_module(modulename)



with open(inputpath, 'r',encoding='UTF8') as f:
    pos = 0
    for line in f:
        job.map_func(pos, line)

    job.switchPhase()

    for k, v in job.shuffle.items():
        job.reduce_func(k, v)

with open(outputpath, 'w', encoding='utf-8') as f:
    for k, v in job.result:
        f.write(f"{k}\t{v}\n")
