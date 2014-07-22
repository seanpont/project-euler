"""
Project Euler Problem #49
==========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""


from utils import *
from collections import defaultdict

sieve = PrimeSieve(10000)

perms = defaultdict(list)


def contains_sequence(items):
    items.sort()
    for i, a in enumerate(items[:-2]):
        for j, b in enumerate(items[i+1:-1]):
            c = b + b - a
            if c in items[j+1:]:
                return a, b, c


for prime in sieve:
    if prime < 1000: continue
    perms[''.join(sorted(str(prime)))].append(prime)

for perm in perms:
    seq = contains_sequence(perms[perm])
    if seq and seq[0] != 1487:
        print ''.join(map(str, seq))



