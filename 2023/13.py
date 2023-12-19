import os

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)


def parse(data):
    patterns = [[list(_) for _ in p.split('\n')] for p in data.split('\n\n')]
    
    return patterns


ref_lines = {}

def reflect(pattern, pid, direction='v', ):
    N = len(pattern[0])
    for i in range(1,N):
        if all(all(a==b for a,b in zip(r[:i][::-1], r[i:])) for r in pattern):
            
            rid = f'{direction}{i}'
            if ref_lines.get(pid) == rid:
                # skip cached 
                continue
            ref_lines[pid] = rid
            return i
        
    rpattern = [[r[i] for r in pattern] for i in range(N)]
    if direction == 'v':
        ref = reflect(rpattern, pid, direction='h')
        if ref:
            return 100*ref


def solve_a(data):
    answer = sum(reflect(p,i) for i,p in enumerate(data))
    return answer

def solve_b(data):
    s = 0
    for pid, p in enumerate(data):
        ref = 0
        for i in range(len(p)):
            for j in range(len(p[0])):
                p[i][j] = '#' if p[i][j] == '.' else '.'
                ref = reflect(p,pid)
                if ref:
                    s+=ref
                    break
                p[i][j] = '#' if p[i][j] == '.' else '.'
            if ref: break
        # if ref: break
    return s

# answer_a_example = solve_a(puzzle.examples[0].input_data)
# print(answer_a_example, puzzle.examples[0].answer_a, answer_a_example == puzzle.examples[0].answer_a)

# PATTERNS = parse(puzzle.examples[0].input_data)
PATTERNS = parse(puzzle.input_data)

answer_a = solve_a(PATTERNS)
print(answer_a)
# puzzle.answer_a = answer_a


# answer_b_example = solve_b(puzzle.examples[0].input_data)
# print(answer_b_example, puzzle.examples[0].answer_b, answer_b_example == puzzle.examples[0].answer_b)

answer_b = solve_b(PATTERNS)
print(answer_b)
puzzle.answer_b = answer_b