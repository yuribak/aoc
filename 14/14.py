poly, Is = open('input').read().split("\n\n")

inserts = {}
for _ in Is.strip().split("\n"):
    k, v = _.strip().split(" -> ")
    inserts[k] = v

CACHE = {}

from collections import Counter


def f(poly, steps):

    if not poly:
        return Counter()
    if steps == 0:
        s = Counter(poly)
        # print(" " * (PRINT_OFFSET - (steps * 2)), f"{poly} => {s}")
        return s
    if len(poly) > 2:
        # print(" "*(PRINT_OFFSET-(steps*2)),f"{poly} = {poly[:2]} + {poly[1:]}")
        s = f(poly[:2], steps) + f(poly[1:], steps) - Counter([poly[1]])
    if len(poly) == 2:
        if (poly, steps) in CACHE:
            # print(" " * (PRINT_OFFSET - (steps * 2)), f"{poly} => [[CACHE]]")
            return CACHE[(poly, steps)]
        i = f"{poly[0]}{inserts[poly]}{poly[1]}" if poly in inserts else poly
        # print(" "*(PRINT_OFFSET-(steps*2)),f"{poly} => {i}")
        s = f(i, steps - 1)
        # print(" " * (PRINT_OFFSET - (steps * 2)), f"{i} => {s}")
    CACHE[poly, steps] = s
    return s

PRINT_OFFSET=20
c = f(poly, 0)
print(max(c.values()) - min(c.values()))
PRINT_OFFSET=80
c = f(poly, 40)
print(max(c.values()) - min(c.values()))
