"""
Project Euler Problem #3
=========================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from utils import prime_factors


target = 600851475143
print max(prime_factors(target))
