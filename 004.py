"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import *


def is_palindrome(num):
    num_str = str(num)
    length = len(num_str)
    for i in xrange(length/2):
        if num_str[i] != num_str[-i-1]:
            return False
    return True


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

