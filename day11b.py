#!/usr/bin/env python3

from collections import defaultdict

example_input = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

def parse(inp):
    nexts = {}
    for line in inp.splitlines():
        l, r = line.split(': ')
        rr = r.split(' ')
        nexts[l] = set(rr)
    return nexts

with open('inputs/day11.input.txt') as f:
    real_input = f.read()

def invert(g):
    inv = defaultdict(set)
    for k, vv in g.items():
        for v in vv:
            inv[v].add(k)
    return inv

def topo_sort(g):
    """Kahn's algorithm, I believe."""
    nexts = {}
    for k, vv in g.items():
        nexts[k] = set(vv)
    prevs = invert(nexts)
    nodes = set(nexts.keys()) | set(prevs.keys())
    S = set(nexts.keys()) - set(prevs.keys())
    L = []
    while S:
        n = S.pop()
        L.append(n)
        while nexts.get(n,None):
            m = nexts[n].pop()
            if not nexts[n]:
                del(nexts[n])
            prevs[m].remove(n)
            if not prevs[m]:
                S.add(m)
    assert not nexts, f'graph has cycles: {nexts}'
    return L

def count_paths(g, topo):
    ways = defaultdict(int)
    ways[topo[0]] = 1
    for n in topo:
        for m in g.get(n, []):
            ways[m] += ways[n]
    return ways[topo[-1]]

def run(inp):
    g = parse(inp)
    top = topo_sort(g)
    pos = {n: i for i, n in enumerate(top)}
    a, b = sorted([pos['dac'], pos['fft']])
    return count_paths(g, top[:a+1]) * count_paths(g, top[a:b+1]) * count_paths(g, top[b:])
assert (got := run(example_input)) == 2, got

print(run(open('inputs/day11.input.txt').read()))
