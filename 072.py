"""
Project Euler Problem #72
==========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d 1,000,000?
"""

from utils import *


class PrimeFactorizor(object):
    def __init__(self, max_size):
        self.sieve = PrimeSieve(max_size+1)
        self.cache = {1: ()}

    def factorize(self, n):
        assert n < self.sieve.size, "Please increase PrimeFactorizor size"
        if n == 0:
            return ()
        if self.sieve.is_prime(n):
            return n,
        if self.cache.get(n) is not None:
            return self.cache[n]
        factors = []
        target = n
        for p in self.sieve:
            while n % p == 0:
                factors.append(p)
                n /= p
                if self.sieve.is_prime(n):
                    factors.append(n)
                    n = 1
                if n != 1 and self.cache.get(n) is not None:
                    factors += self.cache[n]
                    n = 1
                if n == 1:
                    pfs = tuple(factors)
                    self.cache[target] = pfs
                    return pfs

    def totient(self, n):
        pfs = set(self.factorize(n))
        return n * product_of(pf-1 for pf in pfs) / product_of(pfs)


def solve(n):
    factorizor = PrimeFactorizor(n)
    return sum((factorizor.totient(x) for x in xrange(2, n+1)))


print solve(int(1e6))
