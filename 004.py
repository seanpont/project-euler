"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import *
from itertools import combinations

def is_palindrome(num):
    num_str = str(num)
    length = len(num_str)
    for i in xrange(length/2):
        if num_str[i] != num_str[-i-1]:
            return False
    return True


def find_partition(factors):
    total = product(factors)
    for r in range(len(factors)/2+1):
        for combo in combinations(factors, r):
            p1 = product(combo)
            if 100 <= p1 < 1000:
                p2 = total / p1
                if 100 <= p2 < 1000:
                    return p1, p2


max_num = 999 * 999
min_num = 800 * 800
sieve = PrimeSieve(1000)
for p in xrange(max_num, min_num, -1):
    if not is_palindrome(p):
        continue
    factors = prime_factors(p, sieve=sieve)
    # print p, factors
    if max(factors) > 999:
        continue
    # find a partition of factors such that the product of each set is < 1000
    partition = find_partition(factors)
    if partition:
        print p
        break

