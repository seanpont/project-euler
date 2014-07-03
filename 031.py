"""
Project Euler Problem #31
==========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def make_change(amount, coin):
    if coin == 0:
        return 1
    return sum(make_change(amount-contribution, coin-1)
               for contribution in xrange(0, amount+1, coins[coin]))

print make_change(200, len(coins)-1)