import os
import re
from copy import copy
from functools import reduce
from operator import gt, lt, mul

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH, "w") as fout:
        fout.write(puzzle.input_data)


ATTRS = "xmas"


def parse(data):
    wfs, parts = data.split("\n\n")

    parts = [p[1:-1].split(",") for p in parts.split("\n")]
    parts = [tuple(int(a.split("=")[1]) for a in p) for p in parts]

    wfs = [_.split("{") for _ in wfs.split("\n")]
    wfs = [(wf, rules[:-1].split(",")) for wf, rules in wfs]
    for _, rules in wfs:
        for j in range(len(rules) - 1):
            cond, tgt = rules[j].split(":")
            attr, op, value = re.match("(\w+)([<>])(\d+)", cond).groups()
            op = gt if op == ">" else lt
            rules[j] = (attr, op, int(value), tgt)
        rules[-1] = ("x", lambda x, y: True, 1, rules[-1])
    wfs = {wf: rules for wf, rules in wfs}

    return wfs, parts


def check(rules, part):
    for attr, op, value, tgt in rules:
        if op(part[ATTRS.index(attr)], value):
            return tgt


def solve_a(data):    
    wfs, parts = parse(data)

    s = 0
    for part in parts:
        wf = "in"
        while True:
            rules = wfs[wf]
            match check(rules, part):
                case "A": break
                case "R": break
                case wf: continue
        if check(rules, part) == "A":
            s += sum(part)
    return s


def check_b(rules, part):
    
    results = []
    base = copy(part)

    for attr, op, value, tgt in rules:
        a = base[ATTRS.index(attr)]
        passed = set(_ for _ in a if op(_, value))
        p = copy(base)
        p[ATTRS.index(attr)] = passed
        results.append((p, tgt))
        base[ATTRS.index(attr)] = a - passed

    return results


def solve_b(data):
    wfs, _ = parse(data)

    super_part = [set(range(1, 4001)) for _ in range(4)]
    q = [(super_part, "in")]
    accepted = 0

    while q:
        part, wf = q.pop()
        rules = wfs[wf]
        for new_part, tgt in check_b(rules, part):
            match tgt:
                case "A": accepted += reduce(mul, map(len, new_part), 1)
                case "R": continue
                case wf: q.append((new_part, tgt))
    return accepted


# answer_a_example = solve_a(puzzle.examples[0].input_data)
# print(answer_a_example, puzzle.examples[0].answer_a, str(answer_a_example) == puzzle.examples[0].answer_a)

answer_a = solve_a(puzzle.input_data)
print(answer_a)
puzzle.answer_a = answer_a


# answer_b_example = solve_b(puzzle.examples[0].input_data)
# print(answer_b_example, puzzle.examples[0].answer_b, str(answer_b_example) == puzzle.examples[0].answer_b)

answer_b = solve_b(puzzle.input_data)
print(answer_b)
puzzle.answer_b = answer_b
