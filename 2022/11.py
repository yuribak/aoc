f = "2022/input/" + __file__.split('/')[-1].split('.')[0]


with open(f) as fin:
    data = fin.read().split("\n\n")

monkeys = []
p = 1
for mtext in data:
    attrs = mtext.split("\n")
    items = [int(_.strip()) for _ in attrs[1].split(":")[-1].split(",")]
    op, val = attrs[2].split("old ")[-1].split(" ")
    test = int(attrs[3].split()[-1])
    true_tgt = int(attrs[4].split()[-1])
    false_tgt = int(attrs[5].split()[-1])
    monkeys.append((items, op, val, test, true_tgt, false_tgt))
    p *= test

from collections import Counter
from operator import add, mul

c = Counter()
for r in range(10000):
    for i, monkey in enumerate(monkeys):
        items, op, val, test, true_tgt, false_tgt = monkey
        while items:
            c[i] += 1
            item = items.pop(0)
            x = item if val == "old" else int(val)
            item = [mul, add][op == "+"](item, x)
            item = item % p
            # item = int(item/3)
            monkeys[[true_tgt, false_tgt][bool(item % test)]][0].append(item)

a, b = c.most_common(2)
print(a[1] * b[1])
