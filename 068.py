"""
Project Euler Problem #68
==========================

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.

                             4
                              3
                             1 2 6
                            5

Working clockwise, and starting from the group of three with the
numerically lowest external node (4,3,2 in this example), each solution
can be described uniquely. For example, the above solution can be
described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11,
and 12. There are eight solutions in total.

        Total          Solution Set
        9              4,2,3; 5,3,1; 6,1,2
        9              4,3,2; 6,2,1; 5,1,3
        10             2,3,5; 4,5,1; 6,1,3
        10             2,5,3; 6,3,1; 4,1,5
        11             1,4,6; 3,6,2; 5,2,4
        11             1,6,4; 5,4,2; 3,2,6
        12             1,5,6; 2,6,4; 3,4,5
        12             1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the
maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible
to form 16- and 17-digit strings. What is the maximum 16-digit string for
a "magic" 5-gon ring?

     x
       x   x
     x   x
   x  x x x
       x

"""

from utils import *
from itertools import permutations


sacred_triples = [(0, 1, 2), (3, 2, 4), (5, 4, 6), (7, 6, 8), (9, 8, 1)]


def five_gon_it(digits):
    start = min_index(pick(digits, [0, 3, 5, 7, 9]))
    a = []
    for i in xrange(5):
        a.append(pick(digits, sacred_triples[(i+start) % 5]))
    return tuple(flatten(a))


def five_gonners():
    for perm in permutations(range(1, 11)):
        if all_equal(sum(pick(perm, triple)) for triple in sacred_triples):
            yield five_gon_it(perm)


print max((''.join(map(str, gon)) for gon in five_gonners()))


