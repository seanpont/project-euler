"""
Project Euler Problem #65
==========================

The square root of 2 can be written as an infinite continued fraction.

2 = 1 +          1
        2 +        1
            2 +      1
                2 +    1
                    2 + ...

The infinite continued fraction can be written, 2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, 23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions
for square roots provide the best rational approximations. Let us consider
the convergents for 2.

1 + 1 = 3/2
    2

1 +   1   = 7/5
    2 + 1
        2

1 +     1     = 17/12
    2 +   1
        2 + 1
            2

1 +       1       = 41/29
    2 +     1
        2 +   1
            2 + 1
                2

Hence the sequence of the first ten convergents for 2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378,
...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10^th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100^th convergent of the
continued fraction for e.
"""


def e_terms(length):
    yield 2
    for n in xrange(1, length/3+3):
        yield 1
        yield n*2
        yield 1


def solve(size):
    terms = list(e_terms(size))[:size]
    terms.reverse()
    n, d = 1, terms[0]
    for a in terms[1:]:
        n, d = d, n + d * a
    return d, n


from utils import to_digits
print sum(to_digits(solve(100)[0]))