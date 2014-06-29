"""
Project Euler Problem #9
=========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# x^2 + y^2 = z^2
# x + y + z = 1000
# x^2 + y^2 = (1000 - x - y)^2
# 2xy - 2000x - 2000y = -1000000

# axy + bx + cy = d
# (ax+c)(ay+b) = ad+bc

# To solve this diophantine equation, we find all factors of the right side
# and solve for x and y and see if they are integers.
# Note: It so happens that we need the negative factors to find the
# solution to this problem.

from utils import *

a, b, c, d = 2, -2000, -2000, -1000000
right_side = a*d + b*c

for f1, f2 in factor_pairs(right_side):
    f1 = -f1
    f2 = -f2
    if (f1 - c) % a == 0 and (f2 - b) % a == 0:
        x = (f1 - c) / a
        y = (f2 - b) / a
        if 0 < x < 1000 and 0 < y < 1000:
            z = int((x**2 + y ** 2) ** 0.5)
            print x * y * z
