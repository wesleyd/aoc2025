#!/usr/bin/env python3

def is_invalid(n):
    s = str(n)
    l = len(s)//2
    return s[0:l] == s[l:]

def invalids(rang):
    l, r = [int(x) for x in rang.split('-')]
    for n in range(l,r+1):
        if is_invalid(n):
            yield n
assert (got := list(invalids('11-22'))) == [11,22], got
assert (got := list(invalids('95-115'))) == [99], got
assert (got := list(invalids('998-1012'))) == [1010], got
assert (got := list(invalids('1188511880-1188511890'))) == [1188511885], got
assert (got := list(invalids('222220-222224'))) == [222222], got
assert (got := list(invalids('1698522-1698528'))) == [], got
assert (got := list(invalids('446443-446449'))) == [446446], got

def invalids_multi(inp):
    for rang in inp.split(','):
        yield from invalids(rang)

def run(multi):
    return sum(invalids_multi(multi))

assert (got := run('11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124')) == 1227775554, got

print(run(open('inputs/day02.input.txt').read()))
