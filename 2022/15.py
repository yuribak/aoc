import re

p = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    data = []
    for line in fin:
        data.append(tuple(map(int,re.match(p,line).groups())))


def add_range(rs: list,a,b,i=0):
    while True:
        if i>=len(rs):
            rs.append((a,b))
            return
        if b < rs[i][0]:
            rs.insert(i,(a,b))
            return
        s,e = rs[i]
        if s <= a <= b <=e:
            return
        if a<=e+1 and b>=s-1:
            rs.pop(i)
            a,b = min(a,s),max(b,e)
            continue
        i+=1



def manhatan(i,j,x,y):
    return abs(i-x)+abs(j-y)

dists = {(sx,sy): manhatan(sx,sy,bx,by) for sx,sy,bx,by in data}

def sensor_row(sx,sy,bx,by,n):
    dyn = abs(sy-n)
    d= dists[(sx,sy)]
    if dyn <= d:
        return max(sx-(d-dyn), mn), min(sx+d-dyn, mx)

def coverage(n):
    c = []
    for _ in data:
        r = sensor_row(*_,n)
        if r:
            add_range(c,*r) 
    return c


mn=0
mx=4000000


import time
T=time.time()
TS = time.time()
for n in range(mx,mn,-1):
    if n%100000==0:
        # print(times)
        print(time.time()-TS,time.time()-T, n)
        T=time.time()
    c=coverage(n)
    if c != [(0, mx)]:
        s = sum(abs(a-b)+1 for a,b in c)
        if c[0][0] > mn:
            x = 0
        else:
            x = c[0][1]+1
        print(x,n, s, c, x*mx+x)
        break


            



####B######################
