#!/usr/bin/env python3

example_input = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def run(inp):
    lines = inp.splitlines()
    width = len(lines[0])
    verticals = []
    for col in range(width-1,-1,-1):
        ss = []
        for row in range(len(lines)):
            if col < len(lines[row]):
                c = lines[row][col]
            else:
                c = ' '
            if c.isdigit() or c in '*+':
                ss.append(c)
        verticals.append(''.join(ss))
    ret = []
    numbers = []
    for v in verticals:
        if not v:
            continue
        if v[-1] in '+*':
            op = v[-1]
            v = v[:-1]
        else:
            op = ''
        numbers.append(int(v))
        if op == '+':
            ret.append(sum(numbers))
            numbers = []
        elif op == '*':
            product = 1
            for n in numbers:
                product *= n
            ret.append(product)
            numbers = []
    return sum(ret)
assert (got := run(example_input)) == 3263827, got

print(run(open('inputs/day06.input.txt').read()))
