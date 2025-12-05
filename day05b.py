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

def merge_ranges(ranges):
    if not ranges:
        return ranges
    ranges.sort()
    ret = []
    p = ranges[0]
    for r in ranges[1:]:
        if p[1] < r[0]:
            ret.append(p)
            p = r
        else:
            p = (p[0], max(p[1], r[1]))
    ret.append(p)
    return ret

def run(inp):
    s1, _ = inp.split('\n\n')
    ranges = merge_ranges(parse_ranges(s1))
    n = 0
    for r in ranges:
        n += r[1] - r[0] + 1
    return n

assert (got := run(example_input)) == 14, got

print(run(open('inputs/day05.input.txt').read()))
