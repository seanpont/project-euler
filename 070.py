"""
Project Euler Problem #70
==========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""


from utils import *


limit = 10**7
sieve = PrimeSieve(limit**.55)


def slow_totient(n):
    return count(xrange(1, n), lambda x: greatest_common_divisor(x, n, sieve) == 1)


def faster_totient(n):
    factors = sorted(tuple(set(prime_factors(n, sieve))))
    c, a = n, -1
    for i in xrange(len(factors)):
        for f_set in itertools.combinations(factors, i+1):
            c += n/product_of(f_set) * a
        a *= -1
    return c


def solve():
    """ This was not fast enough """
    best_n = 0
    min_ratio = limit
    for n in range(2, limit):
        t = faster_totient(n)
        if sorted(to_digits(n)) == sorted(to_digits(t)) and n/float(t) < min_ratio:
            print n, t, n/float(t), sorted(tuple(set(prime_factors(n, sieve))))
            min_ratio, best_n = n/float(t), n
    print best_n

# solve()


def solve2():
    """So the trick here is that a number with a high totient that is a permutation
    of itself will have only two prime factors. This is because the totient of a prime
    is itself minus one, which will never be a permutation of the number.
    So we need to find a number with as few prime factors as possible."""
    best_n = 0
    min_ratio = limit

    for p1 in sieve:
        for p2 in sieve:
            if p2 >= p1:
                break
            n = p1 * p2
            if n > limit:
                break
            t = (p1-1) * (p2-1)
            if (sorted(to_digits(n)) == sorted(to_digits(t)) and
                n/float(t) < min_ratio):
                # print n, t, n/float(t), sorted(tuple(set(prime_factors(n, sieve))))
                min_ratio, best_n = n/float(t), n
    print best_n


solve2()







