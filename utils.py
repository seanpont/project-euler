__author__ = 'sean'


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
    return factors


def product(nums):
    ans = 1
    for num in nums:
        ans *= num
    return ans


def factor_pairs(target, sieve=None):
    from itertools import combinations
    factors = prime_factors(target, sieve)
    history = set()
    for r in range(len(factors)/2+1):
        for combo in combinations(factors, r):
            p1 = product(combo)
            if p1 in history: continue
            p2 = target / p1
            history.add(p1)
            history.add(p2)
            yield p1, p2


def all_equal(items):
    return len(set(items)) == 1


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


