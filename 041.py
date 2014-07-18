"""
Project Euler Problem #41
==========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils import *
from itertools import permutations


sieve = PrimeSieve(987654321**.5)

for prime_len in xrange(9, 1, -1):
    for perm in permutations(range(prime_len, 0, -1)):
        if is_prime(from_digits(perm), sieve):
            print from_digits(perm)
            exit()
