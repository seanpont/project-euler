"""
Project Euler Problem #34
==========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from utils import *
from math import factorial
from itertools import combinations_with_replacement as combos

factorials = [factorial(i) for i in xrange(10)]

good = []

for n in xrange(2, 7):
    for combo in combos(range(10), n):
        s = sum((factorials[i] for i in combo))
        digits = to_digits(s)
        if len(digits) != n: continue
        if combo == tuple(sorted(digits)):
            good.append(s)

print sum(good)


