with open('2023/input/3') as fin:
    lines = fin.readlines()
    lines = [_.strip() for _ in lines]


from collections import defaultdict


def touching_symbol(i,j):
    s = {}
    for di in (-1,0,1):
        for dj in (-1,0,1):
            if di==dj==0: continue
            if not (0 <= i+di < len(lines) and 0 <= j+dj < len(lines[0])):
                continue
            c = lines[i+di][j+dj]
            if c != '.' and c not in '0123456789':
                s[(i+di,j+dj)] = c
    return s



s = ''
symbol = {}
parts = []
gears = defaultdict(list)
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c in '0123456789':
            s+=c
            symbol.update(touching_symbol(i,j))
        else:
            if s:
                if symbol:
                    parts.append(int(s))
                    for ij, symb in symbol.items():
                        if symb == '*':
                            gears[ij].append(int(s))
                symbol = {}
                s = ''
    if s:
        if symbol:
            parts.append(int(s))
            for ij, symb in symbol.items():
                if symb == '*':
                    gears[ij].append(int(s))
        symbol = {}
        s = ''
# print(parts)
print(sum(parts))

# print(gears)
gear_sum = 0
for parts in gears.values():
    if len(parts) == 2:
        gear_sum += parts[0]*parts[1]

# for gear in sorted(gears):
    # print(gear,gears[gear])
print(gear_sum)

                
            