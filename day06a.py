#!/usr/bin/env python3

example_input = """\
123 328  51 64 
45 64  387 23 
6 98  215 314
*   +   *   +  
"""

def apply(op, nums):
    total = 0 if op == '+' else 1
    while nums:
        num = nums.pop()
        if op == '+':
            total += num
        elif op == '*':
            total *= num
    return total

def run(inp):
    lines = [line.split() for line in inp.splitlines()]
    ops = lines.pop()
    total = 0
    while ops:
        total += apply(ops.pop(), [int(line.pop()) for line in lines])
    return total

assert (got := run(example_input)) == 4277556, got

print(run(open('inputs/day06.input.txt').read()))
