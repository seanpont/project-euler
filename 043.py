"""
Project Euler Problem #43
==========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


from utils import *


def sub_numbers(digits):
    return (from_digits(digits[n:n+3]) for n in xrange(7, 0, -1))


divisors = [2, 3, 5, 7, 11, 13, 17]
divisors.reverse()


def is_valid(digits):
    if digits[5] % 5 != 0: return False
    for i, sub in enumerate(sub_numbers(digits)):
        if sub % divisors[i] != 0:
            return False
    return True


print sum((from_digits(digits) for digits in permutations(to_digits(1234567890)) if is_valid(digits)))





