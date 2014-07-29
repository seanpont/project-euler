"""
Project Euler Problem #51
==========================

By replacing the 1^st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""


from utils import *
from collections import defaultdict


def remove_digits_if_same(num, indices):
    digits = to_digits(num)
    if not all_equal([digits[i] for i in indices]):
        return None
    digits = list(digits)
    for i in reversed(indices):
        digits.pop(i)
    return from_digits(digits)

def add_stars(number, indices):
    starred = list(str(number))
    for i in indices:
        starred.insert(i, '*')
    return ''.join(starred)


assert remove_digits_if_same(4820494, [0, 4]) == 82094
assert add_stars(82094, [0, 4]) == '*820*94'


def patternate(seq, free_indices):
    patterns = defaultdict(list)
    for n in seq:
        digits = remove_digits_if_same(n, free_indices)
        if not digits:
            continue
        patterns[digits].append(n)
    best_pattern = max(patterns, key=lambda k: len(patterns[k]))
    return add_stars(best_pattern, free_indices), patterns[best_pattern]


primes = PrimeSieve(1000000)

for num_free_indices in range(1, 4):
    for free_indices in itertools.combinations(range(5), num_free_indices):
        pattern, patterned_primes = patternate(SequenceInRange(primes, int(1e5), int(1e6)), free_indices)
        if len(patterned_primes) == 8:
            print patterned_primes[0]


