#!/usr/bin/env python3

example_input = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

class Grid:
    def __init__(self, inp):
        self.g = inp.splitlines()
        self.height = len(self.g)
        self.width = len(self.g[0])
    def at(self, row, col):
        if row < 0 or len(self.g) <= row or col < 0 or len(self.g[row]) <= col:
            return '.'
        return self.g[row][col]
    def run(self):
        num_accessible = 0
        for row in range(len(self.g)):
            for col in range(len(self.g[row])):
                if self.at(row,col) != '@':
                    continue
                num_adjacent = 0
                for r in (-1, 0, 1):
                    for c in (-1, 0, 1):
                        if not(r or c):
                            continue
                        if self.at(row+r, col+c) == '@':
                            num_adjacent += 1
                if num_adjacent < 4:
                    num_accessible += 1
        return num_accessible

assert (got := Grid(example_input).run()) == 13, got

print(Grid(open('inputs/day04.input.txt').read()).run())
