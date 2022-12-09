wires = open('input').readlines()

from collections import  Counter
from itertools import chain

c = Counter(list(chain(*[list(map(len,map(str.strip,wire.split("|")[1].split(" ")))) for wire in wires])))
print(sum(c[x] for x in [2,3,4,7]))

def common(s1,s2):
    return len(set(s1).intersection(set(s2)))

z = 0
S = 0
for wire in wires:
    # print(wire)
    code = {}
    rcode = {}
    values = wire.split("|")[0].strip().split(" ")

    # simple digits
    d = None
    for v in values:
        match len(v):
            case 2: d=1
            case 3: d=7
            case 4: d=4
            case 7: d=8
            case _: continue
        sv = "".join(sorted(v))
        code[d]=sv
        rcode[sv]=d

    # advanced:
    for v in values:
        if len(v) == 5:
            if common(v,code[7]) == 2 and common(v,code[4]) == 2:
                d = 2
            elif common(v,code[7]) == 3 and common(v,code[4]) == 3:
                d = 3
            elif common(v,code[7]) == 2 and common(v,code[4]) == 3:
                d = 5
        elif len(v)==6:
            if common(v,code[1]) == 1:
                d = 6
            elif common(v, code[4]) == 3:
                d = 0
            elif common(v, code[4]) == 4:
                d = 9
        else: continue
        sv = "".join(sorted(v))
        code[d] = sv
        rcode[sv] = d

    nums = wire.split("|")[1].strip().split(" ")
    n = int("".join(str(rcode["".join(sorted(v))]) for v in nums))
    S+=n


    # print(len([v for v in values if len(v) in [2,3,4,7]]))
    # print(n)
    # print()
print(S)

