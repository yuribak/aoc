f="input/7"
with open(f) as fin:
    data = [_.strip() for _ in fin]


root = {'..':None}
cwd = root

for line in data:
    if line.startswith("$"):
        cmd, *tgt = line[2:].split()
        if cmd == "cd":
            tgt = tgt[0]
            if tgt.startswith('/'):
                cwd = root
                for _ in tgt.split('/'):
                    if _:cwd = cwd[_]
            else:
                if tgt not in cwd:
                    cwd[tgt] = {'..':cwd}
                cwd = cwd[tgt]
    else:
        attr, name = line.split()
        if attr == "dir":
            if name not in cwd:
                cwd[name] = {'..':cwd}
        else:
            cwd[name] = int(attr)

def dir_sizes(r, test, S):
    s = 0
    for k,v in r.items():
        if k=='..':continue
        if type(v) == int:
            s+= v
        else:
            _, S = dir_sizes(v, test, S)
            if test(_):
                S.append(_)
            s+= _    
    return s, S


root_size, S = dir_sizes(root, lambda _: _<=100000, [])
print(sum(S))

req_size = root_size - 40000000
_, S = dir_sizes(root,lambda _:  _ >= req_size, [])
print(min(S))