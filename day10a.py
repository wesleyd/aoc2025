#!/usr/bin/env python3

# Brute force!

import itertools

from dataclasses import dataclass

example_input = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

@dataclass
class Machine:
    goal: tuple
    buttons: tuple
    start: tuple
    def __init__(self, line):
        pieces = line.split(' ')
        self.goal = tuple([ 1 if c == '#' else 0 for c in pieces[0][1:-1] ])
        self.buttons = tuple(tuple(int(x) for x in piece[1:-1].split(',')) for piece in pieces[1:-1])
        self.start = tuple([0] * len(self.goal))

def click(machine, presses):
    st = list(machine.start)
    for p in presses:
        for b in p:
            st[b] = (st[b] + 1)%2
    return tuple(st)

def solve(machine):
    n = 1
    while True:
        for p in itertools.combinations_with_replacement(machine.buttons, n):
            st = click(machine, p)
            if st == machine.goal:
                return n
        n += 1

def run(inp):
    total = 0
    for line in inp.splitlines():
        m = Machine(line)
        n = solve(m)
        total += n
    return total

assert (got := run(example_input)) == 7, got

print(run(open('inputs/day10.input.txt').read()))
