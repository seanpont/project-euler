"""
Project Euler Problem #63
==========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def num_digits(n):
    c = 0
    while n:
        n /= 10
        c += 1
    return c

assert num_digits(4024) == 4


def find_powers_of_length(length):
    n, p = 1, 1
    while num_digits(p) <= length:
        if num_digits(p) == length:
            yield n
        n += 1
        p = n**length


def solve():
    count = 0
    for length in xrange(1, 50):
        count += len(tuple(find_powers_of_length(length)))
    print count

solve()