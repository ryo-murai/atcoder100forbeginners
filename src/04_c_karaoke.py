import itertools
from typing import List


def max_point(pt: List[List[int]], m):
    ptmax = 0
    for (m1, m2) in itertools.combinations(range(m), 2):
        p = sum([max(p[m1], p[m2]) for p in pt])
        if p > ptmax:
            ptmax = p
    return ptmax


n, m = map(int, input().split(" "))
pt: List[List[int]] = []
for i in range(n):
    p = [int(mx) for mx in input().split(" ")]
    assert len(p) == m
    pt.append(p)

print(max_point(pt, m))
