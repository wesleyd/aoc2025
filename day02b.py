#!/usr/bin/env python3

def repeated(s, m):
    """True if the first n chars of s are repeated."""
    assert m < len(s), f'Aiee! m={m} >= len(s)={len(s)}'
    if len(s) % m != 0:
        return False
    target = s[:m]
    for k in range(1, len(s)//m):
        if s[k*m:(k+1)*m] != target:
            return False
    return True
repeated('565656',2)

def is_invalid(num):
    s = str(num)
    n = len(s)
    for m in range(1, len(s)//2+1):
        if len(s) % m != 0:
            continue
        if repeated(s, m):
            return True
    return False

def invalids(rang):
    l, r = [int(x) for x in rang.split('-')]
    for n in range(l,r+1):
        if is_invalid(n):
            yield n

assert (got := list(invalids('11-22'))) == [11,22], got
assert (got := list(invalids('95-115'))) == [99, 111], got
assert (got := list(invalids('998-1012'))) == [999, 1010], got
assert (got := list(invalids('1188511880-1188511890'))) == [1188511885], got
assert (got := list(invalids('222220-222224'))) == [222222], got
assert (got := list(invalids('1698522-1698528'))) == [], got
assert (got := list(invalids('446443-446449'))) == [446446], got
assert (got := list(invalids('38593856-38593862'))) == [38593859], got
assert (got := list(invalids('565653-565659'))) == [565656], got
assert (got := list(invalids('824824821-824824827'))) == [824824824], got
assert (got := list(invalids('2121212118-2121212124'))) == [2121212121], got

def invalids_multi(inp):
    for rang in inp.split(','):
        yield from invalids(rang)

def run(multi):
    return sum(invalids_multi(multi))

assert (got := run('11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124')) == 4174379265, got

print(run(open('inputs/day02.input.txt').read()))
