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
    return data.strip().split(',')

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def solve_a(data):
    data = parse(data)
    return sum(hash(step) for step in data)


def solve_b(data):
    data = parse(data)
    boxes = [dict() for _ in range(256)]
    for step in data:
        if step.endswith('-'):
            label = step[:-1]
            lenses = boxes[hash(label)]
            if label in lenses:
                lenses.pop(label)
        else:
            label, focal = step.split('=')
            focal = int(focal)
            lenses = boxes[hash(label)]
            lenses[label] = focal
        
    s = 0
    for b in range(len(boxes)):
        for l,focal in enumerate(boxes[b].values()):
            s += (b+1)*(l+1)*focal

    return s

# print(hash('HASH'))
# answer_a_example = solve_a(puzzle.examples[0].input_data)
# print('example a:',answer_a_example, puzzle.examples[0].answer_a, str(answer_a_example) == puzzle.examples[0].answer_a)

# answer_a = solve_a(puzzle.input_data)
# print('answer a:', answer_a)
# puzzle.answer_a = answer_a


answer_b_example = solve_b(puzzle.examples[0].input_data)
print('example b:',answer_b_example, puzzle.examples[0].answer_b, str(answer_b_example) == puzzle.examples[0].answer_b)

answer_b = solve_b(puzzle.input_data)
print('example b:',answer_b)
puzzle.answer_b = str(answer_b)