"""
Project Euler Problem #66
==========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""


def continued_fraction_of_root(n, max_iter=1000):
    """Returns the continued fraction expansion of root(n) - from problem 64"""
    root = n ** .5  # root(23)
    a = int(root)  # a_0
    yield a
    nm, dr = 1, -a
    for _ in xrange(max_iter):
        d = (n - dr**2) / nm
        a = int((root - dr) / d)
        dr, nm = -dr - a * d, d
        yield a


assert list(continued_fraction_of_root(114, 6)) == [10, 1, 2, 10, 2, 1, 20]


def value_of_continued_fraction(terms):
    n, d = 0, 1
    for term in reversed(terms):
        n, d = d, n + d * term
    return d, n


assert value_of_continued_fraction([1, 2, 2]) == (7, 5)


def approx_root(n):
    cf = []
    for a in continued_fraction_of_root(n):
        cf.append(a)
        yield value_of_continued_fraction(cf)


def thanks_lagrange(n):
    for x, y in approx_root(n):
        if x*x - n*y*y == 1:
            return x


vals = [(n, thanks_lagrange(n)) for n in xrange(1, 1001) if n**.5 != int(n**.5)]
print max(vals, key=lambda a: a[1])[0]

