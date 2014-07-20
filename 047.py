"""
Project Euler Problem #47
==========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""


from utils import *


limit = 200000

sieve = PrimeSieve(limit ** .5 + 1)

size = 4
n = 640
count = 0
while n < limit:
    if len(set(prime_factors(n, sieve))) != size:
        count = 0
    else:
        count += 1
    if count == size:
        print n - size + 1
        exit()
    n += 1

