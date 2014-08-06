"""
Project Euler Problem #37
==========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import *

max_n = 1000000

sieve = PrimeSieve(max_n)

def is_prime(n):
    return sieve.is_prime(n)

def left_truncate(n):
    s = str(n)
    for i in xrange(len(s)):
        yield int(s[i:])


def is_truncatable_prime(n):
    return is_prime(n) and \
           match_all(by_tens(n), is_prime) and \
           match_all(left_truncate(n), is_prime)


print sum([n for n in xrange(11, max_n) if is_truncatable_prime(n)])
