with open('input') as fin:
    cukes = [l.strip() for l in fin.readlines()]

east, south = set(), set()
for i in range(len(cukes)):
    for j in range(len(cukes[i])):
        if cukes[i][j] == '>':
            east.add((i, j))
        elif cukes[i][j] == 'v':
            south.add((i, j))

s = 0
while True:
    print(s,end='\r')
    new_east = {(i, (j + 1)%len(cukes[i])) if (i, (j + 1)%len(cukes[i])) not in east and (i, (j + 1)%len(cukes[i]))not in south else (i,j) for i,j in east}
    new_south = {((i+1)%len(cukes), j) if((i+1)%len(cukes), j) not in new_east and ((i+1)%len(cukes), j) not in south else (i,j) for i, j in south }
    s += 1
    if east == new_east and south == new_south:
        break
    east, south = new_east, new_south

print(s)
