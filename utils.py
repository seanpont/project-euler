__author__ = 'sean'

from collections import defaultdict, deque
from itertools import *
import math


# ===== PRIMES AND FACTORS =========================

class PrimeSieve(object):
    def __init__(self, size):
        self.index = 1  # for iteration
        self.size = int(size)
        self.sieve = [True] * self.size
        for i in xrange(2, self.size):
            if not self.sieve[i]:
                continue
            for j in xrange(i+i, self.size, i):
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


def proper_divisors(target, sieve=None):
    factors = prime_factors(target, sieve)
    return tuple(set(chain(*((product_of(combo) for combo in combinations(factors, r)) for r in xrange(len(factors))))))


def factor_pairs(target, sieve=None):
    for f1 in sorted(proper_divisors(target, sieve)):
        f2 = target/f1
        if f2 < f1: break
        yield f1, f2


def greatest_common_divisor(a, b, sieve=None):
    if not sieve:
        sieve = PrimeSieve(math.ceil(max(a, b) ** .5))
    factors_a = prime_factors(a, sieve)
    factors_b = prime_factors(b, sieve)
    common_factors = [fact for fact in factors_a if fact in factors_b]
    return product_of(common_factors)


# ===== LIST HELPERS ==============================


def product_of(nums):
    return reduce(lambda a, b: a*b, nums, 1)


def all_equal(items):
    a = items[0]
    for b in items[1:]:
        if a != b:
            return False
    return True


def all_different(items):
    return len(set(items)) == len(items)


def all_meet_criteria(items, func):
    for item in items:
        if not func(item):
            return False
    return True


def min_index(items):
    return items.index(min(items))


def flatten(iterable):
    return chain(*iterable)


def is_palindrome(items):
    if isinstance(items, int):
        items = str(items)
    s = len(items)-1
    for i in xrange(len(items)/2):
        if items[i] != items[s-i]:
            return False
    return True


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


# ===== PASCAL ==============================


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


def by_tens(n):
    while n > 0:
        yield n
        n /= 10


# ===== DIGITS ==============================

def to_digits(n):
    return tuple(reversed([n % 10 for n in by_tens(n)]))


def from_digits(digits):
    return reduce(lambda a, b: a*10+b, digits)

def rotations(n):
    digits = deque(to_digits(n))
    for i in xrange(len(digits)):
        yield from_digits(digits)
        digits.rotate()

# ===== TESTS ==============================


if __name__ == '__main__':
    assert prime_factors(0, PrimeSieve(3)) == ()
    assert proper_divisors(10) == (1, 2, 5)
    assert tuple(factor_pairs(24)) == ((1, 24), (2, 12), (3, 8), (4, 6))
    assert tuple(factor_pairs(64)) == ((1, 64), (2, 32), (4, 16), (8, 8))
    assert not all_equal([1, 1, 1, 2])
    assert all_equal([4, 4, 4])
    assert is_palindrome('4567654')
    assert product_of([3, 5, 7]) == 3 * 5 * 7
    assert to_digits(48195) == (4, 8, 1, 9, 5)
    assert from_digits(to_digits(830285)) == 830285
    assert list(rotations(345)) == [345, 534, 453]
