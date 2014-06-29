"""
Project Euler Problem #6
=========================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def sum_of_squares(num):
    return sum((i**2 for i in range(1, num+1)))

def square_of_sum(num):
    return sum(range(1, num+1))**2

a = 100
print square_of_sum(a) - sum_of_squares(a)

