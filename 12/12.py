caves = open('input').readlines()

from collections import defaultdict

links = defaultdict(set)
for c in caves:
    a, b = c.strip().split('-')
    links[a].add(b)
    links[b].add(a)

stack = [['start']]
paths = []
while stack:
    head = stack.pop()

    for b in links[head[-1]]:

        if b == 'end':
            paths.append(head + [b])
            continue
        if b.islower() and b in head:
            continue
        stack.append(head + [b])

print(len(paths))

stack = [(['start'], False)]
paths = []
while stack:
    head, signal = stack.pop()

    for b in links[head[-1]]:

        if b == 'end':
            paths.append(head + [b])
            # print(paths[-1])
            continue
        if b == 'start': continue

        if b.islower() and b in head:
            if not signal:
                stack.append((head + [b], True))
            continue
        stack.append((head + [b], signal))

print(len(paths))

def dfs(r, visited):
    if r == 'end':
        # print(visited+['end'])
        return 1
    return sum(dfs(b, visited + [r]) for b in links[r] if (b not in visited or b.isupper()))


def dfs2(r, visited, signal):
    if r == 'end':
        # print(visited+['end'])
        return 1

    return sum(
        dfs2(b, visited + [r], (b.islower() and b in visited) or signal) for b in links[r] if (
            (
                b not in visited
                or b.isupper()
                or (b in visited and not signal)
            ) and b != 'start'
        )
    )


# print(dfs('start', []))
# print(dfs2('start', [], False))

