"""
Project Euler Problem #50
==========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


from utils import *


primes = list(PrimeSieve(1e6))


cheat_sheet = [prime for prime in [0] + primes[:1000]]
for i in xrange(1, len(cheat_sheet)):
    cheat_sheet[i] += cheat_sheet[i-1]

bookmark = 0


def find_consecutive_sum(n, min_count=0):
    global bookmark
    tail = 0
    while cheat_sheet[bookmark] < n:
        bookmark += 1
    head = bookmark
    n -= cheat_sheet[head]
    while head - tail >= min_count:
        # print n, tail, head, sum(primes[tail:head])
        if n > 0:
            n -= primes[head]
            head += 1
        elif n < 0:
            n += primes[tail]
            tail += 1
        elif n == 0:
            return head-tail
    return 0


best_prime, best_count = 0, 0
for prime in primes:
    count = find_consecutive_sum(prime, best_count)
    if count > best_count:
        # print prime, count
        best_prime, best_count = prime, count

print best_prime







