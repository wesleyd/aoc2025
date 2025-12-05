#!/usr/bin/env python3

example_input = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def parse_ranges(inp):
    ret = []
    for line in inp.splitlines():
        a, b = line.split('-')
        ret.append((int(a), int(b)))
    return ret

def fresh(ranges, ingredient):
    for a, b in ranges:
        if a <= ingredient and ingredient <= b:
            return True
    return False

def run(inp):
    s1, s2 = inp.split('\n\n')
    ranges = parse_ranges(s1)
    ingredients = [int(s) for s in s2.splitlines()]
    nfresh = 0
    for ingredient in ingredients:
        if fresh(ranges, ingredient):
            nfresh += 1
    return nfresh
assert (got := run(example_input)) == 3, got

print(run(open('inputs/day05.input.txt').read()))
