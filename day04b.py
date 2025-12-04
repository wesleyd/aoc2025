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
        self.g = [list(line) for line in inp.splitlines()]
        self.height = len(self.g)
        self.width = len(self.g[0])
    def at(self, row, col):
        if row < 0 or len(self.g) <= row or col < 0 or len(self.g[row]) <= col:
            return '.'
        return self.g[row][col]
    def num_rolls(self):
        return sum(line.count('@') for line in self.g)
    def num_adjacent_rolls(self, row, col):
        n = 0
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                if not(r or c):
                    continue
                if self.at(row+r, col+c) == '@':
                    n += 1
        return n
    def run1(self):
        to_remove = set()
        for row in range(len(self.g)):
            for col in range(len(self.g[row])):
                if self.at(row,col) != '@':
                    continue
                if self.num_adjacent_rolls(row,col) < 4:
                    to_remove.add((row,col))
        n = len(to_remove)
        for row, col in to_remove:
            assert self.g[row][col] == '@', f'({row},{col}) != @'
            self.g[row][col] = '.'
        return n
    def run(self):
        total = 0
        while True:
            n = self.run1()
            if n == 0:
                break
            total += n
            #print(f'  Removed {n} rolls of paper')
        return total
assert(Grid(example_input).run()) == 43

print(Grid(open('inputs/day04.input.txt').read()).run())
