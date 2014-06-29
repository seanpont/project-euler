"""
Project Euler Problem #9
=========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# x^2 + y^2 = z^2
# x + y + z = 1000
# x^2 + y^2 = (1000 - x - y)
# 2xy - 2000x - 2000y + 1000000 = 0
# (2x-2000)(2y-2000)=2*1000000 + -2000*-2000
# (2x-2000)(2y-2000)=6000000

# (ax+c)(ay+b)=ad+bc

from utils import *
from itertools import combinations

a, b, c, d = 2, -2000, -2000, 1000**2
right_side = a*d + b*c


factors = prime_factors(d)

for r in range(len(factors)/2+1):
    for combo in combinations(factors, r):
        p1 = product(combo)
        p2 = right_side / p1
        if (p1 - c) % a == 0 and (p2 - b) % a == 0:
            x = (p1 - c) / a
            y = (p2 - b) / a
            print x, y