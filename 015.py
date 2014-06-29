"""
Project Euler Problem #15
==========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""


from utils import pascals_triangle

row = tuple(pascals_triangle(20*2))[-1]
print row[len(row)/2]

