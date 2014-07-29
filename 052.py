"""
Project Euler Problem #52
==========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""


from utils import *


def p52(n):
    for x in xrange(1, 7):
        yield set(to_digits(n*x))


for n in xrange(1, 1000000):
    if all_equal(tuple(p52(n))):
        print n
        exit()