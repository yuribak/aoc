import re
from itertools import  product
import time

p = r"Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)"

f = "2022/input/" + __file__.split('/')[-1].split('.')[0]


tunnels={}
rates = {}
states = {}

with open(f) as fin:
    data = []
    for line in fin:
        m = re.match(p,line)
        s, r, ts = m.groups()
        tunnels[s] = [_.strip() for _ in ts.split(",")]
        rates[s] = int(r)


pos = {k:i for i,k in enumerate(sorted(rates))}
for t in list(tunnels):
    tunnels[pos[t]] = [pos[_] for _ in tunnels[t]]

for r in list(rates):
    rates[pos[r]] = rates[r]

def routes(s, state):
    for t in tunnels[s]:
        yield t
        
    if s not in state and rates[s] > 0:
        yield s

rpos = {v:k for k,v in pos.items()}

c = {'state_cache_miss':0, 'state_cache_hit':0, 'rate_cache_hit':0,'rate_cache_miss':0,'pruned':0}
state_cache = {}
def get_states(ss,state):
    key = (ss,state)
    if key not in state_cache:
        c['state_cache_miss']+=1
        res = []
        for ts in product(*[routes(s,state) for s in ss]):
            # both can't open same valve
            if len(set(ss+ts))==1:
                continue
            r = 0
            tstate = tuple(state)
            for s,t in zip(ss,ts):
                if s==t:
                    tstate = tuple(sorted(tstate + (t,)))
                    r += rates[t]
            if (tuple(ts[::-1]),tstate,r) not in res:
                res.append((tuple(ts),tstate,r))
        state_cache[key] = tuple(res)
    c['state_cache_hit']+=1
    return state_cache[key]


rate_cache = {}
pcache = {}

T = time.time()
def flow():    
            
    MX = 0
    q = [((0,0),26,0,tuple(),[])]
    Q = 0
    _T = time.time()    
    while q:
        if Q%1000000 == 0:
            print(Q,":",MX,c, time.time()-_T)
            _T = time.time()
        Q+=1

        ss, m, mx, state, path = q.pop()
        MX = max(mx, MX)

        if m <= 1 or len(state) == len(rates):
            continue        
        
        key = (ss,state,m)
        if key in rate_cache:
            c['rate_cache_hit']+=1
            continue
        if key not in pcache:
            top = sorted([k for k in range(len(rates)//2) if k not in state], reverse=True, key=lambda _ : rates[_])[:m]
            potential = 0
            for i in range(len(top)//2):            
                potential += rates[top[i*2]]*((m-(1 if top[i*2] in ss else 2)-(i*2)))
                potential += rates[top[i*2+1]]*((m-(1 if top[i*2+1] in ss else 2)-(i*2)))
            pcache[key] = potential
        if mx+pcache[key] < MX :
            c['pruned']+=1
            continue

            
        c['rate_cache_miss']+=1
        


        for tt,tstate,r in get_states(ss, state):

            q.append((tt,m-1, mx+r*(m-1),tuple(tstate), path+[ss]))

        rate_cache[key] = 1

    return MX

print(flow())
print(time.time()-T)