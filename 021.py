"""
Project Euler Problem #21
==========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


from utils import *

sieve = PrimeSieve(1000)

def d(n):
    return sum(proper_divisors(n, sieve))

limit = 10000

ds = [d(n) for n in range(limit)]

# Find pairs by looking ahead in the array.
# ie all numbers to left of cursor have been paired.
pairs = []
for index, dval in enumerate(ds):
    if limit > dval > index == ds[dval]:
        pairs.append((index, dval))

print sum(flatten(pairs))
