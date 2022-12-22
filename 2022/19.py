f = "2022/input/" + __file__.split("/")[-1].split(".")[0]

import re

p = r"Blueprint \d+: Each ore robot costs (\d+ ore). Each clay robot costs (\d+ ore). Each obsidian robot costs (\d+ ore and \d+ clay). Each geode robot costs (\d+ ore and \d+ obsidian)."


with open(f) as fin:
    blueprints = []
    for line in fin:
        m = re.match(p, line.strip())
        bp = []
        for s in m.groups():
            bot = {}
            for ore_cost in s.split(" and "):
                ore, cost = ore_cost.split()
                cost = ["ore", "clay", "obsidian", "geode"].index(cost)
                bot[cost] = int(ore)
            bp.append(bot)
        blueprints.append(bp)
# print(blueprints)


def robots(n, blueprint):

    stats = {
        "cache hit": 0,
        "cache miss": 0,
        "pruned": 0,
        "branches": 0,
    }

    cache = {}

    def affordable_bots(resources):
        if resources not in cache:
            stats["cache miss"] += 1
            res = []

            for botidx, botcost in enumerate(blueprint):
                # if bot is affordable
                if all(resources[ridx] >= cost for ridx, cost in botcost.items()):
                    # reduce bot cost
                    nr = [
                        resources[i] - botcost.get(i, 0) for i in range(len(resources))
                    ]
                    res.append((botidx, tuple(nr)))
            cache[resources] = tuple(res)
        stats["cache hit"] += 1
        return cache[resources]

    q = [(0, (1, 0, 0, 0), (0, 0, 0, 0))]
    seen = set(q)
    MAX = 0
    states = 0
    while q:

        states += 1
        if states % 1000000 == 0:
            print(states, MAX, len(q), stats)

        i, bots, resources = q.pop()

        if i == n:
            MAX = max(resources[-1], MAX)
            stats["branches"] += 1
            continue
        if resources[-1] + sum(range(bots[-1], bots[-1] + n - i)) <= MAX:
            stats["pruned"] += 1
            continue

        nop = (i + 1, bots, tuple(r + b for r, b in zip(resources, bots)))

        if nop not in seen:
            q.append(nop)
            seen.add(nop)

        # manufacture bots
        for botidx, nresources in affordable_bots(resources):

            # don't built more bots than consumable resources
            if botidx < len(bots) - 1:
                if bots[botidx] >= max(b.get(botidx, 0) for b in blueprint):
                    continue

            # mine resources with existing bots
            nresources = tuple(r + b for r, b in zip(nresources, bots))

            # add bot to state
            bots = list(bots)
            bots[botidx] += 1

            state = (i + 1, tuple(bots), nresources)
            if state not in seen:
                seen.add(state)
                q.append(state)
    return MAX



results = []
for i, bp in enumerate(blueprints):
    x = robots(24, bp)
    print('--',i+1,x,bp)
    results.append((i + 1, x))

# print(results)
print(sum(i * x for i, x in results))

results = []
for i, bp in enumerate(blueprints[:3]):
    x = robots(32, bp)
    print("--", i + 1, x, bp)
    results.append((i + 1, x))

from functools import reduce
from operator import mul, itemgetter

# print(results)
print(reduce(mul, map(itemgetter(1), results)))
