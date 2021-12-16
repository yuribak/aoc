from itertools import islice
from math import prod
from operator import gt, lt, eq

packets = open('input').read()


def stream(packets):
    for _ in packets:
        yield from "{0:b}".format(int(_, 16)).zfill(4)


def readint(s, n):
    return int(''.join(next(s) for _ in range(n)), 2)


def readstr(s, n):
    return ''.join(next(s) for _ in range(n))


def _gt(args):
    return gt(*args)


def _lt(args):
    return lt(*args)


def _eq(args):
    return eq(*args)


opmap = dict(zip([0, 1, 2, 3, 5, 6, 7, ], [sum, prod, min, max, _gt, _lt, _eq]))


def read_packet(s, indent=''):
    version = readint(s, 3)
    typeid = readint(s, 3)
    if typeid == 4:
        lit = read_lit(s)
        print(indent, f"({lit})")
        return lit
    else:
        print(indent, f"{opmap[typeid].__name__} [")
        subpackets = read_op(indent, s)
        print(indent, "]")
        return opmap[typeid](subpackets)


def read_op(indent, s):
    lentype = readint(s, 1)
    subpackets = []
    if lentype:
        subpcount = readint(s, 11)
        subpackets[:] = [read_packet(s, indent=indent + '    ') for _ in range(subpcount)]
    else:
        subplen = readint(s, 15)
        ss = islice(s, subplen)
        while True:
            try:
                subpackets.append(read_packet(ss, indent=indent + '    '))
            except RuntimeError as e:
                if isinstance(e.__cause__, StopIteration): break
                raise e
    return subpackets


def read_lit(s):
    lit = []
    while True:
        flag, *bits = readstr(s, 5)
        lit.extend(bits)
        if flag == '0':
            return int(''.join(lit), 2)


print(read_packet(stream(packets)))
