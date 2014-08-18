"""
Project Euler Problem #62
==========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""

from collections import defaultdict
from utils import to_digits
cubes = defaultdict(list)

for n in xrange(10000):
    cube_list = cubes[tuple(sorted(to_digits(n ** 3)))]
    cube_list.append(n)

cubists = filter(lambda c: len(c) >= 5, cubes.values())
print min(map(lambda c: min(c), cubists)) ** 3



