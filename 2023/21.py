import os
from collections import defaultdict

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH, "w") as fout:
        fout.write(puzzle.input_data)


def parse(data):
    data = data.split("\n")
    rocks = set()
    start = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            match data[i][j]:
                case ".": continue
                case "#":
                    rocks.add((i, j))
                case "S":
                    start = (i, j)

    return len(data), len(data[0]), rocks, start


def solve_a(data, steps=6):
    ROWS, COLS, rocks, start = parse(data)

    def safe(i, j):
        return 0 <= i < ROWS and 0 <= j < COLS

    def nbrs(i, j):
        return [
            (x, y)
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))
            if safe(x, y) and (x, y) not in rocks
        ]

    dist = defaultdict(int)

    q = [(start, 0)]
    visited = set()
    while q:
        (i, j), d = q.pop(0)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        dist[d] += 1
        for n in nbrs(i, j):
            q.append((n, d + 1))

    answer = sum(dist[i] for i in range(steps % 2, steps + 1, 2))
    return answer


def solve_b(data, steps):
    ROWS, COLS, rocks, start = parse(data)
    HALF = ROWS // 2

    
    def nbrs(i, j):
        # no such thing as unsafe coordinates
        return ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))

    dist = defaultdict(int)

    prev = set()
    current = set([start])

    first_diff = defaultdict(list)
    second_diff = defaultdict(list)

    # naive count until 3 map lengths out, to collect enough data for 2nd order diff sequence
    for d in range(ROWS // 2 + ROWS * 3):        
        _d = (d - HALF) % ROWS

        
        dist[d] = len(current)
        # ignore 'skewed' counts/diffs while inside the first map
        if d > HALF:
            first_diff[_d].append((dist[d], dist[d] - dist[d - 1]))
            if len(first_diff[_d]) > 1:
                second_diff[_d].append(
                    first_diff[_d][-1][1] - first_diff[_d][-2][1]
                )

        # enumerate next step gardens
        prev, current = current, set(
            (i, j)
            for _ in current
            for (i, j) in nbrs(*_)
            if (i % ROWS, j % COLS) not in rocks and (i, j) not in prev
        )

    # after 3 map lengths, we have enough diff data
    for d in range(ROWS // 2 + ROWS * 3, steps+1):
        _d = (d - HALF) % ROWS
        m = (d - HALF) // ROWS
        dist[d] = (
            dist[d - 1]
            + first_diff[_d][0][1]
            + second_diff[_d][-1] * (m - bool((d - HALF) % ROWS == 0))
        )

    return sum(dist[i] for i in range(steps % 2, steps + 1, 2))


# answer_a_example = solve_a(puzzle.examples[0].input_data)
# print(answer_a_example, puzzle.examples[0].answer_a, str(answer_a_example) == puzzle.examples[0].answer_a)

# answer_a = solve_a(puzzle.input_data, steps=64)
# print(answer_a)
# puzzle.answer_a = answer_a
# answer_b_example = solve_b(puzzle.examples[0].input_data, steps=1000)
# print(answer_b_example, puzzle.examples[0].answer_b, str(answer_b_example) == puzzle.examples[0].answer_b)

import time

start = time.time()
answer_b = solve_b(puzzle.input_data, steps=26501365)
print(answer_b)
puzzle.answer_b = answer_b
print(time.time() - start)
