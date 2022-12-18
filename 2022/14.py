f = "2022/input/14"

def sign(n): return 1 if n >=0 else -1

def add(a,b): return tuple(x+y for x,y in zip(a,b))

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def trunc(d): return tuple(min(1,abs(_))*sign(_) for _ in d)


import time
with open(f) as fin:
    paths = [[tuple(map(int,_.strip().split(','))) for _ in row.split('->')] for row in fin]

maxx = max((x for path in paths for x,y in path))
minx = min((x for path in paths for x,y in path))
maxy = max((y for path in paths for x,y in path))

space = {}
for path in paths:
    for s,t in zip(path[:-1],path[1:]):
        i = s
        while i!=t:
            space[i] = '#'
            i = add(i,trunc(sub(t,i)))
        space[i] = '#'


def nexta(s):
    for step in ((0,1),(-1,1),(1,1)):
        t= add(s,step)
        if t not in space:
            return t
    return False


T = time.time()
S = (500,0)
spilling = False
p=[S]
while not spilling:
    s = p[-1]
    while t:=nexta(s):
        if not minx <= t[0] < maxx:
            spilling = True
            break
        p.append(t)
        s=t
    if spilling: break
    space[s] = 'o'
    if s == p[-1]:
        p.pop()

print(sum(_=='o' for _ in space.values()))
# a: 817
print(time.time()-T)

def nextb(s):
    for step in ((0,1),(-1,1),(1,1)):
        t= add(s,step)
        if t not in space and t[1]<maxy+2:
            return t
    return False

T = time.time()
p = [S]
while True:
    s = p[-1]
    while t:=nextb(s):
        p.append(t)
        s=t
    space[s] = 'o'
    if s==S:        
        break
    if s==p[-1]:
        p.pop()

print(sum(_=='o' for _ in space.values()))
print(time.time()-T)



# b: 23416