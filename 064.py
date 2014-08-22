"""
Project Euler Problem #64
==========================

All square roots are periodic when written as continued fractions and can
be written in the form:

N = a[0] +            1
           a[1] +         1
                  a[2] +     1
                         a[3] + ...

For example, let us consider 23:

23 = 4 + 23 -- 4 = 4 +  1  = 4 +  1     1     1 +  23 - 3
                                      23--4          7

If we continue we would get the following expansion:

23 = 4 +          1
         1 +        1
             3 +      1
                 1 +    1
                     8 + ...

The process can be summarised as follows:

a[0] = 4,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[1] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[2] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[3] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7
a[4] = 8,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[5] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[6] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[7] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7

It can be seen that the sequence is repeating. For conciseness, we use the
notation 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square
roots are:

2=[1;(2)], period=1
3=[1;(1,2)], period=2
5=[2;(4)], period=1
6=[2;(2,4)], period=2
7=[2;(1,1,1,4)], period=4
8=[2;(1,4)], period=2
10=[3;(6)], period=1
11=[3;(3,6)], period=2
12= [3;(2,6)], period=2
13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N 13, have an odd period.

How many continued fractions for N 10000 have an odd period?
"""


def cycle_counter(gen):
    a = []
    while True:
        n = gen.next()
        if n in a:
            return len(a) - a.index(n)
        a.append(n)


assert cycle_counter([1, 3, 5, 6, 3].__iter__()) == 3
assert cycle_counter([1, 1].__iter__()) == 1


def doodle(n):
    root = n ** .5  # root(23)
    a = int(root)  # a_0
    nm, dr = 1, -a
    for _ in xrange(1000):
        d = (n - dr**2) / nm
        a = int((root - dr) / d)
        dr, nm = -dr - a * d, d
        yield a, nm, dr


def solve():
    count = 0
    for n in xrange(1, 10000):
        if n**.5 == int(n**.5): continue
        if cycle_counter(doodle(n)) % 2 == 1:
            count += 1
    print count


solve()