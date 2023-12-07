import os
import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))

INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH) and puzzle.input_data:
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)

e = puzzle.examples[0]

def solve_a(data):
    seeds_maps = data.split('\n\n')
    seeds = list(map(int,seeds_maps[0].split(':')[1].strip().split()))
    maps = [m.split('\n')[1:] for m in seeds_maps[1:]]
    maps = [[list(map(int,entry.split())) for entry in m] for m in maps]

    def follow(seed, m):
        for dst, src, ln in m:
            if  src <= seed <= src+ln:
                return dst + (seed-src)
        return seed
    
    locations = []
    for s in seeds:
        loc = s
        for m in maps:
            loc = follow(loc,m)
        locations.append(loc)
    return min(locations)
        

def range_subtract(a,b):
    start_a, end_a = a
    start_b, end_b = b
    if end_a < start_b or end_b < start_a:
        # no intersection
        return None, [a]
    if start_a >= start_b and end_a <= end_b:
        # a contained in b
        return a, []
    if start_b >= start_a and end_b <= end_a:
        # b contained in a
        return b, [(start_a, start_b-1), (end_b+1,end_a)]
    if start_a < start_b:
        # a overlaps from the 'left' 
        return (start_b, end_a), [(start_a, start_b-1)]
    if end_a > end_b:
        # a overlaps from the 'right' 
        return (start_a, end_b), [(end_b+1, end_a)]


def solve_b(data):
    seeds_maps = data.split('\n\n')
    seeds = list(map(int,seeds_maps[0].split(':')[1].strip().split()))
    maps = [m.split('\n')[1:] for m in seeds_maps[1:]]
    maps = [[list(map(int,entry.split())) for entry in m] for m in maps]
    # print(seeds)
    # print(maps)

    def follow(seed_ranges, m):
        result = []
        for dst, src, mln in m:
            rs = []
            while seed_ranges:
                a = seed_ranges.pop()
                b = (src, src + mln-1)
                overlap, remainders = range_subtract(a,b)
                if overlap:
                    start_o, end_o = overlap
                    d = dst - src
                    result.append((start_o+d, end_o+d)) 
                if remainders:
                    rs += remainders
            seed_ranges = rs                
        return result+seed_ranges
    
    locations = []
    for i in range(0,len(seeds),2):
        s, ln = seeds[i:i+2]
        locs = [(s,s+ln-1)]
        for m in maps:
            locs = follow(locs,m)
        locations += locs
    return min(locations)[0]

import time
start = time.time()

answer_a = solve_a(puzzle.input_data)
answer_b = solve_b(puzzle.input_data)

print(answer_b, answer_b, time.time()-start)

