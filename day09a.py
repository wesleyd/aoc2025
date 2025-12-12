#!/usr/bin/env python3

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

def parse(inp):
    ret = []
    for line in inp.splitlines():
        a, b = line.split(',')
        ret.append((int(a), int(b)))
    return ret

def run(points):
    max_area = 0
    for i in range(len(points)):
        p = points[i]
        for j in range(i+1, len(points)):
            q = points[j]
            area = (abs(p[0]-q[0])+1) * (abs(p[1]-q[1])+1)
            if area > max_area:
                max_area = area
    return max_area

assert (got := run(parse(example_input))) == 50, got

print(run(parse(open('inputs/day09.input.txt').read())))
