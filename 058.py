"""
Project Euler Problem #58
==========================

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

                           37 36 35 34 33 32 31
                           38 17 16 15 14 13 30
                           39 18  5  4  3 12 29
                           40 19  6  1  2 11 28
                           41 20  7  8  9 10 27
                           42 21 22 23 24 25 26
                           43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""


from utils import *


def spiral(s_max):
    s, n = 0, 1
    yield n
    while s < s_max:
        s += 2
        for _ in xrange(4):
            n += s
            yield n


sieve = PrimeSieve(100000)
spiral_gen = spiral(100000)
spiral_gen.next()  # throw away the 1
primes, total, ratio, s = 0, 1, 1, 1
while ratio >= .1:
    s += 2
    for _ in xrange(4):
        if is_prime(spiral_gen.next(), sieve):
            primes += 1
    total += 4
    ratio = float(primes) / float(total)
    # print primes, total, ratio, s
print s

