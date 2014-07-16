"""
Project Euler Problem #32
==========================

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

from utils import PrimeSieve, factor_pairs, to_digits, all_different

sieve = PrimeSieve(10e4)

def acceptable(digits):
    return 0 not in digits and all_different(digits)

special = []

for n in xrange(100, 10000):
    dn = to_digits(n)
    if not acceptable(dn): continue
    for f1, f2 in factor_pairs(n, sieve):
        df1, df2 = to_digits(f1), to_digits(f2)
        if len(df1) + len(df2) + len(dn) == 9 and acceptable(dn + df1 + df2):
            special.append(n)
            break

print sum(special)



