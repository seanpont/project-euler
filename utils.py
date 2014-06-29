__author__ = 'sean'

from collections import defaultdict
from itertools import *


class PrimeSieve(object):
    def __init__(self, size):
        self.index = 1  # for iteration
        self.size = size
        self.sieve = [True] * size
        for i in xrange(2, size):
            if not self.sieve[i]:
                continue
            for j in xrange(i+i, size, i):
                self.sieve[j] = False

    def is_prime(self, num):
        return self.sieve[num]

    def __call__(self, num):
        return self.is_prime(num)

    def __iter__(self):
        self.index = 1
        return self

    def next(self):
        self.index += 1
        while self.index < self.size and not self.sieve[self.index]:
            self.index += 1
        if self.index >= self.size:
            raise StopIteration()
        return self.index


def prime_factors(target, sieve=None):
    if target == 0:
        return ()
    if not sieve:
        sieve_size = min(10000, int(target ** .5) + 1)
        sieve = PrimeSieve(sieve_size)
    factors = []
    for i in sieve:
        while target % i == 0:
            # print '%s / %s = %s' % (target, i, target / i)
            target /= i
            factors.append(i)
        if target == 1:
            break
    if target > 1:
        factors.append(target)
    return tuple(factors)


def num_divisors(target, sieve=None):
    if not sieve:
        sieve = PrimeSieve(target)
    d = defaultdict(int)
    factors = prime_factors(target, sieve)
    for f in factors:
        d[f] += 1
    return product([v+1 for v in d.values()])


def product(nums):
    ans = 1
    for num in nums:
        ans *= num
    return ans


def proper_divisors(target, sieve=None):
    factors = prime_factors(target, sieve)
    return tuple(set(chain(*((product(combo) for combo in combinations(factors, r)) for r in xrange(len(factors))))))


def factor_pairs(target, sieve=None):
    for f1 in sorted(proper_divisors(target, sieve)):
        f2 = target/f1
        if f2 < f1: break
        yield f1, f2


def all_equal(items):
    a = items[0]
    for b in items[1:]:
        if a != b:
            return False
    return True


def min_index(items):
    return items.index(min(items))


def lowest_common_multiple(nums, max_num=1000000000):
    rangers = [xrange(i, max_num, i).__iter__() for i in nums]
    nexts = [ranger.next() for ranger in rangers]
    while not all_equal(nexts):
        index = min_index(nexts)
        nexts[index] = rangers[index].next()
    return nexts[0]


def _pairs(items):
    pairs, remainder = [(items[i], items[i+1]) for i in xrange(0, len(items)-1, 2)], None
    if len(items) % 2 == 1:
        remainder = items[-1]
    return pairs, remainder


def pairwise_reduce(func, iterable):
    length = len(iterable)
    if length == 1:
        return iterable[0]
    pairs, remainder = _pairs(iterable)
    reduced = [func(*pair) for pair in pairs]
    if remainder:
        reduced.append(remainder)
    return pairwise_reduce(func, reduced)


def _next_pascal_row(p):
    pn = [0]*(len(p)+1)
    pn[0] = pn[-1] = 1
    for i in range(len(p)-1):
        pn[i+1] = p[i] + p[i+1]
    return pn


def pascals_triangle(limit):
    p = [1]
    yield p
    while limit > 0:
        p = _next_pascal_row(p)
        yield p
        limit -= 1


def flatten(iterable):
    return chain(*iterable)


if __name__ == '__main__':
    assert prime_factors(0, PrimeSieve(3)) == ()
    assert proper_divisors(10) == (1, 2, 5)
    assert tuple(factor_pairs(24)) == ((1, 24), (2, 12), (3, 8), (4, 6))
    assert tuple(factor_pairs(64)) == ((1, 64), (2, 32), (4, 16), (8, 8))
    assert not all_equal([1, 1, 1, 2])
    assert all_equal([4, 4, 4])
