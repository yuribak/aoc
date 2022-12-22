import re
from operator import add, sub, mul, truediv
f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

p = r"(\w+): (\w+) ([+-/*]) (\w+)"
monkeys = {}
with open(f) as fin:
    for line in fin:
        m = re.match(p,line)
        if m:
            monkey, left, op, right = m.groups()
            monkeys[monkey] = (left, op, right)
        else:
            monkey, v = line.split(':')
            monkeys[monkey] = int(v)
# print(monkeys)

ops = dict(zip('+-*/',[add,sub,mul,truediv]))
def compute(m):
    data = monkeys[m]
    if isinstance(data, int):
        return data
    left, op, right = data
    return int(ops[op](compute(left), compute(right)))

print(compute('root'))


rops = dict(zip('+-*/',[sub,add,truediv,mul]))

def lambdacompute(m):
    data = monkeys[m]
    if data is None:
        return lambda _:_
    if isinstance(data, int):
        return data
    left, op, right = data
    left, right = lambdacompute(left), lambdacompute(right)
    if callable(left):
        return lambda _: left(rops[op](_,right))
    elif callable(right): 
        if op == '-': return lambda _: right(left-_)
        elif op == '/': return lambda _: right(int(left/_))
        else: return lambda _: right(int(rops[op](_,left)))

    return int(ops[op](left,right))


        
# print(monkeys['root'])
monkeys['humn'] = None
left, _, right = monkeys['root']
try:
    target = compute(left)
    variable = right
except TypeError:
    target = compute(right)
    variable = left

print(lambdacompute(variable)(target))
