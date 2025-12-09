#!/usr/bin/env python3

example_input = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

def distances(jboxes):
    dists = {}
    for i in range(len(jboxes)):
        for j in range(i+1, len(jboxes)):
            j1, j2 = jboxes[i], jboxes[j]
            dx, dy, dz = j1[0] - j2[0], j1[1] - j2[1], j1[2] - j2[2]
            r2 = dx*dx + dy*dy + dz*dz
            dists[(j1,j2)] = r2
    return {key: value for key, value in sorted(dists.items(), key=lambda item: item[1], reverse=True)}

def merge(pools):
    i = 0
    while i < len(pools):
        j = i+1
        while j < len(pools):
            if pools[i].isdisjoint(pools[j]):
                j += 1
                continue
            pools[i] |= pools[j]
            pools = pools[:j] + pools[j+1:]
            i = 0  # $$$ ?
        i += 1
    return pools

def run(inp,n=10):
    junction_boxes = [ tuple(int(n) for n in line.split(',')) for line in inp.splitlines() ]
    dists = distances(junction_boxes)
    pools = []
    for i in range(n):
        pr, dist = dists.popitem()
        a, b = pr
        pools = merge(pools + [set([a, b])])
    sizes = [len(v) for v in pools]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]
assert (got := run(example_input)) == 40, got

print(run(open('inputs/day08.input.txt').read(), n=1000))
