"""
Project Euler Problem #52
==========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

from utils import *


print find(xrange(1, 1000000), lambda n: all_equal((set(to_digits(n*x))) for x in xrange(1, 7)))

