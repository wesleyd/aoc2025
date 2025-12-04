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

def max_joltage(line, n=12):
    if n > len(line):
        return int(line)
    i = 0
    ret = []
    while n:
        j, d = max_both(line[i:len(line)-n+1])
        ret.append(d)
        i += j + 1
        n -= 1
    return int(''.join(ret))
assert (got := max_joltage("987654321111111")) == 987654321111, got
assert (got := max_joltage("811111111111119")) == 811111111119, got
assert (got := max_joltage("234234234234278")) == 434234234278, got
assert (got := max_joltage("818181911112111")) == 888911112111, got

def run(inp):
    return sum(max_joltage(line) for line in inp.splitlines())
assert (got := run(example_input)) == 3121910778619, got

print(run(open("inputs/day03.input.txt").read()))
