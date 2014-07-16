"""
Project Euler Problem #33
==========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from utils import *


def is_curious(numerator, denominator):
    if numerator == denominator or numerator % 10 == 0 and denominator % 10 == 0:
        return False
    dn, dd = list(to_digits(numerator)), list(to_digits(denominator))
    intersect = set(dn).intersection(dd)
    if not intersect:
        return False
    intersect = intersect.pop() # there will always only be one
    dn.remove(intersect)
    dd.remove(intersect)
    d_num = from_digits(dn)
    d_denom = from_digits(dd)
    return numerator * d_denom == d_num * denominator


curious = [(n, d)
           for n in xrange(10, 100)
           for d in xrange(n, 100)
           if is_curious(n, d)]

p = reduce(lambda a, b: (a[0] * b[0], a[1] * b[1]), curious, (1, 1))

gcd = greatest_common_divisor(*p)

print p[1] / gcd




