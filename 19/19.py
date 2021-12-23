from collections import defaultdict
from itertools import combinations, starmap, product, permutations
from operator import sub

Bs = open('input').readlines()
beacons = defaultdict(set)
s = 0
for _ in Bs[1:]:
    if not _.strip():
        continue
    if _.startswith('---'):
        s += 1
        continue
    # scanner id => set(beacons coordinates)
    beacons[s].add(tuple(map(int, _.strip().split(','))))


def dists(bs):
    # beacon coord => set(distance to other beacons)
    ds = defaultdict(set)
    for a, b in combinations(bs, 2):
        _d = tuple(map(abs, starmap(sub, zip(a, b))))
        ds[a].add(_d)
        ds[b].add(_d)
    return ds

def rotations(bs):
    for p in permutations(range(3)):
        if matched: break
        for sign in product([1, -1], [1, -1], [1, -1]):
            yield {(sign[0] * _[p[0]], sign[1] * _[p[1]], sign[2] * _[p[2]]) for _ in bs}

# scanner 0 as anchor
root = 0
droot = dists(beacons[root])
scanners = {(0, 0, 0)}
while len(beacons) > 1:
    print(f"scanners: {len(scanners)}/{s}, beacons: {len(beacons[root])}")
    for scanner in list(beacons.keys()):
        if scanner == 0: continue
        matched = False
        for rotated_bs in rotations(beacons[scanner]):

            # match beacons based on relative internal distances
            ds = dists(rotated_bs)
            matched_bs = []
            for a, b in product(beacons[root], rotated_bs):
                if len(droot[a] & ds[b]) >= 11:
                    matched_bs.append((a, b))

            # confirm orientation offset vector is the same for matched beacons
            offset = set(tuple(starmap(sub, zip(*_))) for _ in matched_bs)
            if len(matched_bs) >= 11 and len(offset) == 1:

                # `offset` is the re-oriented coordinates of scanner
                offset = offset.pop()
                scanners.add(offset)

                # updated beacons to anchor scanner orientation
                beacons[root] |= {(x + offset[0], y + offset[1], z + offset[2]) for x, y, z in rotated_bs}
                print(root, scanner, "-", offset)

                # recalculate relative distances for anchor scanner
                droot = dists(beacons[root])
                del beacons[scanner]
                matched = True
                break

print(max(sum(map(abs, starmap(sub, zip(a, b)))) for a, b in combinations(scanners, 2)))