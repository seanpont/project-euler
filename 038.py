"""
Project Euler Problem #38
==========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from utils import *
import itertools


def test(n, digits):
    n_start = n
    d = to_digits(n)
    while digits and starts_with(digits, d):
        n += n_start
        digits = digits[len(d):]
        d = to_digits(n)
    return len(digits) == 0


def search(digits):
    for n_length in xrange(1, 5):
        n = from_digits(digits[:n_length])
        if test(n, digits):
            return True
    return False

# print test(9, to_digits(918273645))
# print search(to_digits(192384576))

all_digits = range(1, 10)
all_digits.reverse()

for perm in itertools.permutations(all_digits, 9):
    if search(perm):
        print from_digits(perm)
        break


