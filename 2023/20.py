import os
from typing import Any

import aocd
import math

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH, "w") as fout:
        fout.write(puzzle.input_data)


class FlipFlop:
    def __init__(self, name, targets) -> None:
        self.name = name
        self.state = False
        self.targets = targets

    def signal(self, src, pulse):
        if pulse:
            return []
        self.state = not self.state
        return [(self.name, self.state, t) for t in self.targets]

    def hash(self):
        return [self.state]


class Conjunction:
    def __init__(self, name, inputs, targets) -> None:
        self.name = name
        self.inputs = {i: False for i in inputs}
        self.targets = targets

    def signal(self, src, pulse):
        self.inputs[src] = pulse
        out_pulse = not all(self.inputs.values())
        return [(self.name, out_pulse, t) for t in self.targets]

    def hash(self):
        return list(self.inputs.values())


class Broadcast:
    def __init__(self, name, targets) -> None:
        self.name = name
        self.targets = targets

    def signal(self, src, pulse):
        return [(self.name, pulse, t) for t in self.targets]

    def hash(self):
        return []


from collections import defaultdict


def parse(data):
    nodes = {}
    inputs = defaultdict(set)
    for line in data.split("\n"):
        node, targets = line.split("->")
        node = node.strip()
        targets = tuple(_.strip() for _ in targets.split(","))
        node_type = None
        if node[0] in "%&":
            node_type, node = node[0], node[1:]

        match node_type:
            case None:
                assert node == "broadcaster", node
                nodes[node] = Broadcast(node, targets)
            case '%':
                nodes[node] = FlipFlop(node, targets)
            case '&':
                nodes[node] = Conjunction(node, [], targets)
                
        for t in targets:
            inputs[t].add(node)

    for node in nodes:
        if isinstance(nodes[node], Conjunction):
            nodes[node].inputs = {i: False for i in inputs[node]}

    return nodes


def push(nodes):
    q = [("button", False, "broadcaster")]
    pulses = [0, 0]
    while q:
        src, pulse, tgt = q.pop(0)
        pulses[pulse] += 1
        if tgt in nodes:
            q.extend(nodes[tgt].signal(src, pulse))
    return pulses


def solve_a(data):
    nodes = parse(data)
    LOW, HIGH = 0, 0
    for _ in range(1000):
        low, high = push(nodes)
        LOW += low
        HIGH += high

    return LOW * HIGH


def pushb(nodes, target):
    q = [("button", False, "broadcaster")]
    sources = set()
    while q:
        src, pulse, tgt = q.pop(0)
        if tgt in nodes:
            q.extend(nodes[tgt].signal(src, pulse))
        if pulse and tgt == target:
            sources.add(src)
    return sources


def solve_b(data, target="rx"):
    nodes = parse(data)

    second_last = None
    for n in nodes:
        if target in nodes[n].targets:
            second_last = n
            break

    i = 0
    periods = defaultdict(list)
    while True:
        sources = pushb(nodes, second_last)
        for s in sources:
            periods[s].append(i)
        if periods and all(len(c) > 1 for c in periods.values()):
            return math.lcm(*[v[-1] - v[-2] for v in periods.values()])
        i += 1


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
# 244465191362269
