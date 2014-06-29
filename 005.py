"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
from utils import *


def lcm(a, b):
    return lowest_common_multiple((a, b))

rlcm = pairwise_reduce(lcm, range(2, 21))
print rlcm