"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import *


max_num = 999 * 999
min_num = 800 * 800
sieve = PrimeSieve(1000)
for p in xrange(max_num, min_num, -1):
    if not is_palindrome(p):
        continue
    for f1, f2 in factor_pairs(p, sieve):
        if 100 <= f1 < 1000 and 100 <= f2 < 1000:
            print p
            exit()

