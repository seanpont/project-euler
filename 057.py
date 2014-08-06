"""
Project Euler Problem #57
==========================

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

            2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?

1 + 1/2 = (2 + 1) / 2


"""


def expansions(n):
    num, denom = 3, 2
    for _ in xrange(n):
        yield num, denom
        num, denom = num+2*denom, num+denom

from utils import count, to_digits

print count(expansions(1000), lambda x: len(to_digits(x[0])) > len(to_digits(x[1])))