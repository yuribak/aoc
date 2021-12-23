steps = open('input').readlines()

cubiods = []
for s in steps:
    inst, cuboid = s.split(' ')
    cubiods.append((inst, list(tuple(map(int, c.split('=')[1].split('..'))) for c in cuboid.split(','))))
print(cubiods)

coords = {}

from copy import deepcopy
def slice_axis(inst, cuboid, coords, indent=''):
    if not cuboid:
        # print(indent, f"=>{inst}")
        return inst

    a,b = cuboid.pop(0)

    # print(indent, f"{(a,b)}, {cubid}, {sorted(coords.keys())}")
    if not coords:
        # print(indent, f"no coords, new slice: {(a,b)}, {cubid}, ")
        coords[(a,b)] = slice_axis(inst, list(cuboid), dict(), indent=indent + '    ')
        return coords

    pass

    keys = sorted(coords.keys())
    for c,d in keys:
        # (c--d)..(a--b) is strictly greater than current range - skip
        if a > d:
            # print(indent, f"c:{c}---d:{d}..a:{a}----b:{b} - skipping")
            continue

        v = coords.pop((c,d))

        # a portion of (a,b) precedes (c,d) - new cubid
        # (a++b)...[c-d]
        # (a++[c--b)--d]
        # (a++[c--d]--b)
        if a < c:
            # print(indent, f"a:{a}**c:{c}..{[d,b][b>d]}..{[d,b][b<d]} - new slice: {(a,min(b,c-1))}, {cubid}")
            coords[(a,min(b,c-1))] = slice_axis(inst, list(cuboid), dict(), indent=indent + '    ')

        # a portion of (c,d) precedes (a,b) - existing cubid
        # (a++b)...[c-d]
        # (a++[c--b)--d]
        # (a++[c--d]--b)
        if a > c:
            # print(indent, f"c:{c}**a:{a}..{[d, b][b < d]}..{[d, b][b > d]} - existing slice: {(c, min(d,a - 1))}, {cubid}")
            coords[(c, min(d,a - 1))] = deepcopy(v)

        # store inner intersection of a,b & c,d as new intersecting cubid
        if b >= c and a <= d:
            # print(indent, f"c:{c}..a:{a}**{[d, b][b < d]}..{[d, b][b > d]} - merged slice: {(max(a,c),min(b,d))}, {cubid}")
            coords[(max(a,c),min(b,d))] = slice_axis(inst, list(cuboid), deepcopy(v), indent=indent + '    ')
            if b == d:
                # print(indent, '.. and break')
                break

        # a portion of (c,d) succeeds (a,b) - cut cubid
        if b < d:
            # print(indent, f"c:{c}..a:{a}--b:{b}**d:{d} - existing slice and break: {(max(b+1,c), d)}, {cubid}")
            coords[(max(b+1,c), d)] = deepcopy(v)
            break


        # a portion of (a,b) succeeds (c,d) - recurse same level
        if b > d:
            # print(indent, f"c:{c}..a:{a}--d:{d}**b:{b} - update (a,b): {(max(a,d+1),b)}, {cubid}")
            (a,b) = (max(a,d+1),b)
            # coords = slice_axis(inst,[(d+1,b)] + list(cubid), deepcopy(coords))

        for (i,j) in coords.keys():
            assert i<=j

    if a > d:
            # print(indent, f"c:{c}--d:{d}..a:{a}**b:{b} - leftover new slice): {(a, b)}, {cubid}")

            coords[(a,b)] = slice_axis(inst, list(cuboid), dict(), indent=indent + '  ')
    return coords



for i,(inst,c) in enumerate(cubiods):
    print(f"{i}/{len(cubiods)} ] ", inst, c, f"({len(coords)})")
    coords = slice_axis(inst,c,coords)

c = 0
s = 0
for x,vx in coords.items():
    print(x)
    for y,vy in vx.items():
        print('  ',y)
        for z,vz in vy.items():
            # print('    ',z,vz, (x[1] - x[0]+1)* (y[1] - y[0]+1) * (z[1] - z[0]+1))
            if vz == 'on':
                s += 1
                c += (x[1] - x[0]+1)* (y[1] - y[0]+1) * (z[1] - z[0]+1)
print(s,c)

# coords = {}
# for c in [(10,12),(11,13),(9,11)]:
#     print("#####",c, 'on')
#     coords = slice_axis('on',[c],coords)
#
#     for x,vx in coords.items():
#         print(x,vx)
#         # for y,vy in vx.items():
#         #     print('  ',y)
#         #     for z,vz in vy.items():
#         #         print('    ',z,vz, (x[1] - x[0]+1)* (y[1] - y[0]+1) * (z[1] - z[0]+1))
#         #         if vz == 'on':
#         #             c += (x[1] - x[0]+1)* (y[1] - y[0]+1) * (z[1] - z[0]+1)
