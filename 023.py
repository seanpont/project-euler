"""
Project Euler Problem #23
==========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

from utils import *

limit = 28123

prime_sieve = PrimeSieve(1000)

def is_abundant(n):
    return sum(proper_divisors(n, prime_sieve)) > n

abundant_sieve = [False] * limit

for n in xrange(limit):
    if abundant_sieve[n]: continue
    if is_abundant(n):
        for j in xrange(n, limit, n):
            abundant_sieve[j] = True

def has_abundant_adders(n):
    for i in xrange(1, n):
        if abundant_sieve[i] and abundant_sieve[n-i]:
            return True

print sum((n for n in xrange(1, limit) if not has_abundant_adders(n)))

#
# finder = find_adders(abundants)
# print 'identifying numbers than cannot be expressed as the sum of two abundant numbers'
# print sum((i for i in range(limit) if not finder(i)))

