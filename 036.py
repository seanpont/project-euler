"""
Project Euler Problem #36
==========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from utils import *


print sum([n for n in xrange(1000000) if is_palindrome(n) and is_palindrome(bin(n)[2:])])