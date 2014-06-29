"""
Project Euler Problem #14
==========================

The following iterative sequence is defined for the set of positive
integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                         13 40 20 10 5 16 8 4 2 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

_cache_size = 10000000
_cache = [0] * _cache_size
_cache[1] = 1

def cache(n, count=0):
    if n < _cache_size:
        if count > 0:
            _cache[n] = count
        else:
            return _cache[n]
    return 0


def collatz(n):
    while n > 1:
        yield n
        n = n/2 if n % 2 == 0 else 3*n+1
    yield 1


def cached_collatz(start):
    count = 0
    for n in collatz(start):
        if cache(n):
            count += cache(n)
            break
        count += 1
    cache(start, count)
    return count


max_start, max_count = 1, 1
for start in range(2, 1000000):
    count = cached_collatz(start)
    if count > max_count:
        max_start, max_count = start, count

print max_start