import os

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))

puzzle = aocd.models.Puzzle(year=year, day=day)


def solve(data):
    cards = data.split("\n")

    SCORE = 0
    scores = {}
    matches = {}

    for card in cards:
        card_id, numbers = card.split(":")
        card_id = int(card_id.split()[1])
        wins, mine = numbers.split("|")
        wins, mine = [set(map(int, _.strip().split())) for _ in (wins, mine)]
        match = len(wins & mine)
        matches[card_id] = match
        score = 2 ** (match - 1) if match else 0
        scores[card_id] = score
        # print(card_id, wins, mine, score)
        SCORE += score

    for n in range(len(matches), len(matches) - 5, -1):
        assert matches[n] < (220 - n + 1)

    C = {i: 1 for i in range(1, len(matches) + 1)}

    # for each card
    for i in range(1, len(matches) + 1):
        m = matches[i]
        # for each of the following `m` cards
        for j in range(i + 1, i + 1 + m):
            # bump card count by the number of `i` cards
            # because each instance of the `i` card will have `m` matches and produce a single copy of each of (i+1,i+m) cards.
            C[j] += C[i]

        # print(i,C[i], matches[i])
    assert set(C.keys()) == set(range(1, len(matches) + 1))

    return SCORE, sum(C.values())


answer_a, answer_b = solve(puzzle.input_data)
print(answer_a, answer_b)

