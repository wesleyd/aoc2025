#!/usr/bin/env python3

example_input = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""

def max_both(it):
    """Find the index of the max value, and the value."""
    max_index = None
    max_value = None
    for i, c in enumerate(it):
        if max_value is None or c > max_value:
            max_index = i
            max_value = c
    return max_index, max_value

def max_joltage(line):
    i, d1 = max_both(line[:-1])
    _, d2 = max_both(line[i+1:])
    return int(d1 + d2)
assert (got := max_joltage("987654321111111")) == 98, got
assert (got := max_joltage("811111111111119")) == 89, got
assert (got := max_joltage("234234234234278")) == 78, got
assert (got := max_joltage("818181911112111")) == 92, got

def run(inp):
    return sum(max_joltage(line) for line in inp.splitlines())
assert (got := run(example_input)) == 357, got

print(run(open("inputs/day03.input.txt").read()))
