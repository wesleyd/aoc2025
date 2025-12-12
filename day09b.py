#!/usr/bin/env python3

from dataclasses import dataclass

from collections import defaultdict

example_input = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

def sign(x):
    if x > 0:
        return +1
    if x < 0:
        return -1
    return 0

@dataclass
class Grid:
    points: list
    rows: list
    cols: list
    heights: list
    widths: list
    row_lookup: dict
    col_lookup: dict
    gpoints: list
    grid: list
    def __init__(self, inp):
        self.points = [ tuple(int(x) for x in reversed(line.split(','))) for line in inp.splitlines() ]
        self.rows = sorted(set(p[0] for p in self.points))
        self.cols = sorted(set(p[1] for p in self.points))
        #
        self.row_lookup = {}
        self.heights = [self.rows[0]]
        for i in range(1,len(self.rows)):
            self.row_lookup[self.rows[i-1]] = len(self.heights)
            self.heights.append(1)
            self.heights.append(self.rows[i] - self.rows[i-1] - 1)
        self.row_lookup[self.rows[-1]] = len(self.heights)
        self.heights.append(1)
        #
        self.col_lookup = {}
        self.widths = [self.cols[0]]
        for i in range(1,len(self.cols)):
            self.col_lookup[self.cols[i-1]] = len(self.widths)
            self.widths.append(1)
            self.widths.append(self.cols[i] - self.cols[i-1] - 1)
        self.col_lookup[self.cols[-1]] = len(self.widths)
        self.widths.append(1)
        #
        self.gpoints = [ (self.row_lookup[p[0]], self.col_lookup[p[1]]) for p in self.points ]
        self.grid = [ ['.'] * len(self.widths) for h in self.heights ]
        for p in self.gpoints:
            self.grid[p[0]][p[1]] = 'O'
        ga = self.gpoints[-1]
        for gz in self.gpoints:
            drow = sign(gz[0] - ga[0])
            dcol = sign(gz[1] - ga[1])
            gp = ga
            while gp != gz:
                gp = (gp[0] + drow, gp[1] + dcol)
                self.grid[gp[0]][gp[1]] = '#'
            self.grid[gp[0]][gp[1]] = 'O'
            ga = gz
        for line in self.grid:
            inside = False
            for i, c in enumerate(line):
                if c == '.':
                    if inside:
                        line[i] = '#'
                else:
                    inside = not inside

def run(g):
    partials = []
    for h in g.heights:
        partials.append([0] * len(g.widths))
    if g.grid[0][0] != '.':
        partials[0][0] = g.heights[0] * g.widths[0]
    for col in range(1, len(g.widths)):
        partials[0][col] = partials[0][col-1]
        if g.grid[0][col] != '.':
            partials[0][col] += g.heights[0] * g.widths[col]
    for row in range(1, len(g.heights)):
        partials[row][0] = partials[row-1][0]
        if g.grid[row][0] != '.':
            partials[row][0] += g.heights[row] * g.widths[0]
    for row in range(1, len(g.heights)):
        for col in range(1, len(g.widths)):
            partials[row][col] = partials[row][col-1] + partials[row-1][col] - partials[row-1][col-1]
            if g.grid[row][col] != '.':
                partials[row][col] += g.heights[row] * g.widths[col]
    largest_full_area = 0
    for i in range(len(g.points)):
        p = g.points[i]
        gp = g.gpoints[i]
        for j in range(i+1, len(g.points)):
            q = g.points[j]
            gq = g.gpoints[j]
            top, bottom = sorted((p[0], q[0]))
            left, right  = sorted((p[1], q[1]))
            full_area = (right - left + 1) * (bottom - top + 1)
            gtop, gbottom = sorted((gp[0], gq[0]))
            gleft, gright  = sorted((gp[1], gq[1]))
            above = 0
            area = partials[gbottom][gright] - partials[gtop-1][gright] - partials[gbottom][gleft-1] + partials[gtop-1][gleft-1]
            if area != full_area:
                continue
            if area > largest_full_area:
                largest_full_area = area
    return largest_full_area
assert (got := run(Grid(example_input))) == 24, got

print(run(Grid(open('inputs/day09.input.txt').read())))
