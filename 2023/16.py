import os

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH, "w") as fout:
        fout.write(puzzle.input_data)


def parse(data):
    return data.split("\n")


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def show(data, bs=None):
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            print("*" if (i, j) in bs else data[i][j], end="")
        print()
    print()


def solve_a(data, start):
    data = parse(data)
    ROWS = len(data)
    COLS = len(data[0])

    def safe(i, j):
        return 0 <= i < ROWS and 0 <= j < COLS

    beams = [start]  # (position, direction)
    visited = set()
    while beams:
        bp, bd = beams.pop()
        visited.add((bp, bd))
        # show(data,{bp})

        nbs = []

        match data[bp[0]][bp[1]]:
            case ".":
                nbs.append((add(bp, bd), bd))
            case "-":
                if bd[0] == 0:
                    nbs.append((add(bp, bd), bd))
                else:
                    nbs.append((add(bp, LEFT), LEFT))
                    nbs.append((add(bp, RIGHT), RIGHT))

            case "|":
                if bd[1] == 0:
                    nbs.append((add(bp, bd), bd))
                else:
                    nbs.append((add(bp, UP), UP))
                    nbs.append((add(bp, DOWN), DOWN))
            case "/":
                match bd:
                    # right
                    case (0, 1):
                        nbs.append((add(bp, UP), UP))
                    # down
                    case (1, 0):
                        nbs.append((add(bp, LEFT), LEFT))
                    # up
                    case (-1, 0):
                        nbs.append((add(bp, RIGHT), RIGHT))
                    # left
                    case (0, -1):
                        nbs.append((add(bp, DOWN), DOWN))
            case "\\":
                match bd:
                    # right
                    case (0, 1):
                        nbs.append((add(bp, DOWN), DOWN))
                    # down
                    case (1, 0):
                        nbs.append((add(bp, RIGHT), RIGHT))
                    # up
                    case (-1, 0):
                        nbs.append((add(bp, LEFT), LEFT))
                    # left
                    case (0, -1):
                        nbs.append((add(bp, UP), UP))
        nbs = [(p, d) for (p, d) in nbs if safe(*p) and (p, d) not in visited]
        beams.extend(nbs)

    answer = len(set(p for p, d in visited))
    # show(data,{p for p,d in visited})
    return answer


def solve_b(_data):

    data = parse(_data)
    ROWS = len(data)
    COLS = len(data[0])

    start_b = []
    for i in range(ROWS):
        start_b.append(((i, 0), RIGHT))
        start_b.append(((i, COLS - 1), LEFT))

    for i in range(COLS):
        start_b.append(((0, i), DOWN))
        start_b.append(((ROWS - 1, i), UP))

    answer = max(solve_a(_data, s) for s in start_b)
    return answer


start_a = ((0, 0), (0, 1))
answer_a_example = solve_a(puzzle.examples[0].input_data, start_a)
print(
    answer_a_example,
    puzzle.examples[0].answer_a,
    str(answer_a_example) == puzzle.examples[0].answer_a,
)

answer_a = solve_a(puzzle.input_data, start_a)
print(answer_a)
puzzle.answer_a = answer_a


# answer_b_example = solve_b(parse(puzzle.examples[0].input_data))
# print(answer_b_example, puzzle.examples[0].answer_b, str(answer_b_example) == puzzle.examples[0].answer_b)

answer_b = solve_b(puzzle.input_data)
print(answer_b)
puzzle.answer_b = answer_b
