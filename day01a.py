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
    #print(f'The dial starts by pointing at {at}')
    for rot in rots:
        clicks = int(rot[1:])
        if rot[0] == 'L':
            clicks = 100 - clicks
        at = (at + clicks) % 100
        if at == 0:
            nzeros += 1
        #print(f'The dial is rotated by {rot} to point at {at}')
    return nzeros
assert (got := run(example_input)) == 3, got

print(run(open('inputs/day01.input.txt').read()))
