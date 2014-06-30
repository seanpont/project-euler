"""
Project Euler Problem #27
==========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                                e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""


from utils import *

is_prime = PrimeSieve(20000)

def prime_streak(a, b):
    f = lambda n: n**2 + a*n + b
    n = 0
    while is_prime(f(n)):
        n += 1
    return n

assert prime_streak(1, 41) == 40

best_streak, best_coeff = 0, ()
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        streak = prime_streak(a, b)
        if streak > best_streak:
            best_streak = streak
            best_coeff = (a, b)

print product(best_coeff)


