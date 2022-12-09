
from collections import defaultdict

f="input/5"
with open(f) as fin:
    data = fin.read()

S = defaultdict(list)
stacks, moves = data.split("\n\n")

for line in stacks.split("\n")[-1::-1]:
    for i in range(1,len(line),4):
        if line[i].strip():
            S[((i-1)//4)+1].append(line[i])
    
for move in moves.split('\n'):
    _ = move.split()
    n, s, t = list(map(int,[_[1], _[3], _[5]]))

    S[t].extend(S[s][-n:])
    S[s][-n:] = []
    
print(''.join(v[-1] for k,v in sorted(S.items())))


    