lines = open('input').readlines()

from collections import Counter
from operator import itemgetter, add, sub
from itertools import starmap

def bitadd(x,y):
    return tuple(starmap(add,zip(x,y)))

def bitsub(x,y):
    return tuple(starmap(sub,zip(x,y)))

coords = Counter()
for line in lines:
    src, tgt = (x1,y1),(x2,y2) = [tuple(map(int,_.split(','))) for _ in line.split(' -> ')]
        # if x1 != x2 and y1 != y2:
        #     continue
    # print(src,"=>",tgt)
    d = bitsub(tgt, src)
    d = tuple(0 if _ == 0 else (-1 if _ < 0 else 1) for _ in d)
    s = src
    while s != tgt:
        # print(s)
        coords[s] += 1
        s = bitadd(s,d)
    coords[tgt] += 1

print(len([v for v in coords.values() if v > 1]))

