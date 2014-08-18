"""
Project Euler Problem #61
==========================

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following
formulae:

Triangle     P[3,n]=n(n+1)/2   1, 3, 6, 10, 15, ...
Square       P[4,n]=n^2        1, 4, 9, 16, 25, ...
Pentagonal   P[5,n]=n(3n-1)/2   1, 5, 12, 22, 35, ...
Hexagonal    P[6,n]=n(2n-1)     1, 6, 15, 28, 45, ...
Heptagonal   P[7,n]=n(5n-3)/2   1, 7, 18, 34, 55, ...
Octagonal    P[8,n]=n(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

 1. The set is cyclic, in that the last two digits of each number is the
    first two digits of the next number (including the last number with
    the first).
 2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281),
    and pentagonal (P[5,44]=2882), is represented by a different number in
    the set.
 3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the
set.
"""

from itertools import permutations


def frange(low, hi, func):
    n, res, x = 0, [], func(0)
    while x < hi:
        if x >= low:
            res.append(x)
        n += 1
        x = func(n)
    return res


def are_connected(n, n_next):
    return n % 100 == n_next/100


def find_path(table, n, next_row, endpoint):
    for n_next in table[next_row]:
        if are_connected(n, n_next):
            if next_row == 5:
                if are_connected(n_next, endpoint):
                    return [n, n_next]
            else:
                path = find_path(table, n_next, next_row + 1, endpoint)
                if path:
                    return [n] + path


def solve():
    figurates = [
        frange(1000, 10000, lambda n: n*(n+1)/2),
        frange(1000, 10000, lambda n: n*n),
        frange(1000, 10000, lambda n: n*(3*n-1)/2),
        frange(1000, 10000, lambda n: n*(2*n-1)),
        frange(1000, 10000, lambda n: n*(5*n-3)/2),
        frange(1000, 10000, lambda n: n*(3*n-2)),
    ]

    for perm in permutations(figurates):
        for n in perm[0]:
            path = find_path(perm, n, 1, n)
            if path:
                print sum(path)
                exit()

solve()