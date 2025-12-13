#!/usr/bin/env python3

from collections import defaultdict

example_input = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

def parse(inp):
    nexts = {}
    for line in inp.splitlines():
        l, r = line.split(': ')
        rr = r.split(' ')
        nexts[l] = rr
    return nexts

def find_paths(nexts, st='you', prev=None):
    if prev is None:
        prev = [st]
    for p in nexts[st]:
        path = prev + [p]
        if p == 'out':
            yield path
        else:
            yield from find_paths(nexts, p, path)

def run(inp):
    return sum(1 for _ in find_paths(parse(inp)))
assert (got := run(example_input)) == 5, got

print(run(open('inputs/day11.input.txt').read()))
