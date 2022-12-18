f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    drops = set(tuple(map(int,_.split(','))) for _ in fin)


def adjacent(xyz ,mn=0,mx=None):
    for _ in range(len(xyz)):
        ls = list(xyz)
        ls[_] += 1
        if mx is None or mn <= ls[_] <= mx:
            yield tuple(ls)
        ls[_] -=2
        if mx is None or mn <= ls[_] <= mx:
            yield tuple(ls)

print(6*len(drops) - sum(len(set(adjacent(d))&drops) for d in drops))

# fill bounding cube
N = max(max(_) for _ in drops) + 2
cube = set()
start = (N,N,N)
q = {start}
while q:
    c = q.pop()
    adj = set(adjacent(c,mn=-1,mx=N))
    q |= adj-drops-cube
    cube |= adj - drops


print(sum(len(set(adjacent(d))&drops) for d in cube))

