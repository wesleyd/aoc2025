#!/usr/bin/env python3

example_input = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def run(inp):
    at = 50
    nzeros = 0
    rots = inp.splitlines()
    for rot in rots:
        direction = rot[0]
        clicks = int(rot[1:])
        while clicks:
            if direction == 'L':
                at -= 1
            else:
                at += 1
            if at < 0:
                at += 100
            if at >= 100:
                at -= 100
            if at == 0:
                nzeros += 1
            clicks -= 1
    return nzeros
assert (got := run(example_input)) == 6, got

print(run(open('inputs/day01.input.txt').read()))  # 6067 is too low
