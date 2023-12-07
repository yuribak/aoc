with open('2023/input/2') as fin:
    lines = fin.readlines()

from collections import defaultdict

games= defaultdict(dict)
for line in lines:
    game, rounds = line.split(':')
    gid = game.split()[1]
    # print(gid,':')
    for i,round in enumerate(rounds.split(';')):
        # print('  round',i)
        for cube in round.split(','):
            count, color = cube.split()
            count = int(count)
            current = games.get(gid, {}).get(color,0)
            games[gid][color] = max(count, current)
            # print('    ',color,count)

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

gid_sum=0
for gid in games:
    possible = True
    for color in cubes:
        if color in games[gid] and games[gid][color] > cubes[color]:
            possible = False
            break
    if possible:
        gid_sum += int(gid)
print(gid_sum)

P=0
for gid in games:
    power = 1
    for v in games[gid].values():
        power *= max(v,1)
    P+=power

print(P)

