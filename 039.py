"""
Project Euler Problem #39
==========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

from utils import max_index

triples = [0]*1000

for a in xrange(1, 1000):
    for b in xrange(a, 1000):
        c = (a**2 + b**2)**.5
        p = int(a + b + c)
        if c == int(c) and p < 1000:
            triples[p] += 1

print max_index(triples)
