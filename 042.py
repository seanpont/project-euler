"""
Project Euler Problem #42
==========================

The n^th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt [http://projecteuler.net/project/words.txt], a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?
"""

from string import uppercase


def score_word(word):
    return sum([uppercase.index(letter) for letter in word]) + len(word)

f = open('words.txt')
words = f.readline().split(",")
f.close()

words = map(lambda x: x[1:-1], words)
triangles = [n*(n+1)/2 for n in xrange(1, 100)]

print len([word for word in words if score_word(word) in triangles])


