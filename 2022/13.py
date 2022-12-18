f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    pairs = [[eval(x) for x in _.split("\n")] for _ in fin.read().split('\n\n')]

def compare(left, right):
    if type(left) == int and type(right) == int: return left - right
    if type(left) == list and type(right) == list:
        for l,r in zip(left,right):
            if _:= compare(l,r):
                return _
        return len(left) - len(right)
    l,r = [[_] if type(_) == int else _ for _ in (left, right)]
    return compare(l, r)

print(sum(i+1 for i,(left,right) in enumerate(pairs) if compare(left,right) < 0))

packets = [item for sublist in pairs for item in sublist]
a,b = [[2]],[[6]]
packets.extend([a,b])

from functools import cmp_to_key
packets.sort(key=cmp_to_key(compare))

print((packets.index(a)+1 )*(packets.index(b)+1))