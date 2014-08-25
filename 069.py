"""
Project Euler Problem #69
==========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, f(9)=6.

+------------------------------------------+
| n  | Relatively Prime | f(n) | n/f(n)    |
|----+------------------+------+-----------|
| 2  | 1                | 1    | 2         |
|----+------------------+------+-----------|
| 3  | 1,2              | 2    | 1.5       |
|----+------------------+------+-----------|
| 4  | 1,3              | 2    | 2         |
|----+------------------+------+-----------|
| 5  | 1,2,3,4          | 4    | 1.25      |
|----+------------------+------+-----------|
| 6  | 1,5              | 2    | 3         |
|----+------------------+------+-----------|
| 7  | 1,2,3,4,5,6      | 6    | 1.1666... |
|----+------------------+------+-----------|
| 8  | 1,3,5,7          | 4    | 2         |
|----+------------------+------+-----------|
| 9  | 1,2,4,5,7,8      | 6    | 1.5       |
|----+------------------+------+-----------|
| 10 | 1,3,7,9          | 4    | 2.5       |
+------------------------------------------+

It can be seen that n=6 produces a maximum n/f(n) for n 10.

Find the value of n <= 1,000,000 for which n/f(n) is a maximum.
"""

# We're looking for a large number with few relative primes.
# The number of relative primes is inversely proportional to the
# number of distinct prime factors (I imagined creating a sieve
# for each number), and to mark off as many numbers as possible,
# you want those prime factors to be as small as possible.
# Did I prove it? No. But do I feel clever for figuring it
# out with paper and pencil? Sure do.

print 2 * 3 * 5 * 7 * 11 * 13 * 17

