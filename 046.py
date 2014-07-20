"""
Project Euler Problem #46
==========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""


from utils import *


limit = 10000

sieve = PrimeSieve(limit ** .5)

squares = [i**2 * 2 for i in xrange(1, int(limit ** .5))]

def suits_goldbach(n):
    if is_prime(n, sieve) or n % 2 == 0: return True
    for square in squares:
        if square > n: return False
        if is_prime(n - square, sieve):
            return True
    raise Exception("increase the limit!")


for n in xrange(1, limit):
    if not suits_goldbach(n):
        print n
        exit()

