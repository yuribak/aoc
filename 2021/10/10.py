chunks = open('input').readlines()

match = {
    '{':'}',
    '[':']',
    '<':'>',
    '(':')'
}

test_score = {
    ')':3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def test_chunk(chunk):
    q = []
    for c in chunk:
        if c in '({[<':
            q.append(c)
        elif c in ')}]>':
            d = q.pop()
            if match[d] == c:
                continue
            else:
                return test_score[c]
    return 0

fix_score = {
    ')':1,
    ']': 2,
    '}': 3,
    '>': 4
}
def fix_chunk(chunk):
    q = []
    for c in chunk:
        if c in '({[<':
            q.append(c)
        elif c in ')}]>':
            d = q.pop()
            if match[d] == c:
                continue
            else:
                return 0
    s = 0
    for c in q[::-1]:
        s = s*5 + fix_score[match[c]]

    return s


print(sum(test_chunk(chunk) for chunk in chunks))
fixed_scores = [_ for _ in sorted(fix_chunk(chunk) for chunk in chunks) if _ > 0]
print(fixed_scores[int(len(fixed_scores)/2)])



