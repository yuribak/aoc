f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    data = [_.strip().split() for _ in fin]

def sign(n): return 1 if n >=0 else -1

def add(a,b): return [x+y for x,y in zip(a,b)]

def sub(a,b): return [x-y for x,y in zip(a,b)]

ms = dict(zip('RLUD',[(1,0),(-1,0),(0,1),(0,-1)]))

def ropes(r):
    k = [[0,0] for _ in range(r)]
    T = set()
    T.add(tuple(k[-1]))
    for m,v in data:
        v = int(v)
        dst = add(k[0],[_*v for _ in ms[m]])
        while k[0] != dst:
            k[0] = add(k[0],ms[m])
            for i in range(1,len(k)):
                d = sub(k[i-1],k[i])
                if any(abs(_) > 1 for _ in d):
                    d = [min(1,abs(_))*sign(_) for _ in d]
                    k[i] = add(k[i],d)
                else: break
            T.add(tuple(k[-1]))
    return len(T)

print(ropes(2))
print(ropes(10))
