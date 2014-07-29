"""
Project Euler Problem #53
==========================

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^5C[3] = 10.

In general,

^nC[r] =   n!    ,where r n, n! = n * (n1) * ... * 3 * 2 * 1, and 0! = 1.
         r!(nr)!

It is not until n = 23, that a value exceeds one-million: ^23C[10] =
1144066.

How many values of  ^nC[r], for 1 n 100, are greater than one-million?
"""

from utils import *
from math import factorial as f


print count((f(n) / (f(r) * f(n-r)) for n in xrange(1, 101) for r in xrange(1, n)), lambda x: x > 1000000)