import os
from collections import Counter

import aocd
from functools import cmp_to_key

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH, "w") as fout:
        fout.write(puzzle.input_data)


FIVE_OF_A_KIND = 19
FOUR_OF_A_KIND = 18
FULL_HOUSE = 17
THREE_OF_A_KIND = 16
TWO_PAIR = 15
PAIR = 14
HIGH_CARD = 13

SUITS = dict(zip("23456789TJQKA", range(13)))
JSUITS = dict(zip("J23456789TQKA", range(13)))


def hand_type(hand):
    counts = Counter(hand)
    max_count = counts.most_common(1)[0][1]

    match len(counts):
        case 1:
            return FIVE_OF_A_KIND
        case 2:
            return FOUR_OF_A_KIND if max_count == 4 else FULL_HOUSE
        case 3:
            return THREE_OF_A_KIND if max_count == 3 else TWO_PAIR
        case 4:
            return PAIR
        case 5:
            return HIGH_CARD


def j_hand_type(hand):
    counter = Counter(hand)
    if "J" in hand and len(counter) > 1:
        del counter["J"]
        most_common_non_j = counter.most_common(1)[0][0]
        hand = hand.replace("J", most_common_non_j)
    return hand_type(hand)


def solve_a(data, hand_type=hand_type, SUITS=SUITS):
    def cmp(a, b):
        ha, hb = hand_type(a[0]), hand_type(b[0])
        if ha != hb:
            return ha - hb

        for ca, cb in zip(a[0], b[0]):
            if SUITS[ca] != SUITS[cb]:
                return SUITS[ca] - SUITS[cb]

    data = [line.split() for line in data.split("\n")]
    data = [(hand, int(bid)) for hand, bid in data]

    answer = 0
    for i, (hand, bid) in enumerate(sorted(data, key=cmp_to_key(cmp))):
        answer += bid * (i + 1)

    return str(answer)


def solve_b(data):
    return solve_a(data, hand_type=j_hand_type, SUITS=JSUITS)


answer_a = solve_a(puzzle.input_data)
print(answer_a)
puzzle.answer_a = answer_a


answer_b = solve_b(puzzle.input_data)
print(answer_b)

