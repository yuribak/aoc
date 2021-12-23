from collections import Counter
from itertools import product

players = [int(_.split(':')[1].strip()) for _ in open('input').readlines()]


class Die:

    def __init__(self):
        self.count = 0
        self.die = iter(self)

    def __iter__(self):
        while True:
            yield from iter(range(1, 101))

    def roll(self):
        self.count += 3
        return next(self.die), next(self.die), next(self.die)


d = Die()

scores = [0] * len(players)
p = 0
B = 10
t = 0
while max(scores) < 1000:
    t += 1
    ns = d.roll()
    players[p] = ((players[p] - 1 + sum(ns)) % B) + 1
    scores[p] += players[p]

    p += 1
    p %= len(players)

print(min(scores) * d.count)

CACHE = {}

DIRAK = Counter([sum(_) for _ in product(range(1,4),range(1,4),range(1,4))])


def game(p, players, scores):
    if (p, tuple(players), tuple(scores)) not in CACHE:

        if max(scores) >= 21:
            s = Counter([int(scores[1] > scores[0])])
        else:
            s = Counter()
            for d,e in DIRAK.items():
                _players = list(players)
                _scores = list(scores)
                _players[p] = ((players[p] - 1 + d) % B) + 1
                _scores[p] += _players[p]

                s += {k:v*e for k,v in game((p + 1) % 2, _players, _scores).items()}
        CACHE[(p, tuple(players), tuple(scores))] = s
    return CACHE[(p, tuple(players), tuple(scores))]


players = [int(_.split(':')[1].strip()) for _ in open('input').readlines()]
c = game(0, players, [0] * len(players))
print(c.most_common(1)[0][1])
