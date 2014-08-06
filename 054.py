"""
Project Euler Problem #54
==========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt [http://projecteuler.net/project/poker.txt] contains
one-thousand random hands dealt to two players. Each line of the file contains
ten cards (separated by a single space): the first five are Player 1's cards and
the last five are Player 2's cards. You can assume that all hands are valid (no
invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from utils import *


def card_val(card):
    return '23456789TJQKA'.index(card[0]) + 2


class Hand(object):

    def __init__(self, cards):
        self.cards = cards.split(' ')
        self.values = [card_val(card) for card in self.cards]
        self.values.sort(reverse=True)
        self.suits = set(card[1] for card in self.cards)
        self.value_count = {value: count(self.values, value) for value in self.values}
        self.count_value = defaultdict(list)
        for k in self.value_count:
            self.count_value[self.value_count[k]] += [k]

def high_card(hand):
    return [1] + hand.values

def one_pair(hand):
    if len(hand.count_value[2]) == 1:
        return [2] + hand.count_value[2] + hand.values

def two_pairs(hand):
    if len(hand.count_value[2]) == 2:
        return [3] + sorted(hand.count_value[2], reverse=True) + hand.values

def three_of_a_kind(hand):
    if 3 in hand.count_value:
        return [4] + hand.count_value[3] + hand.values

def straight(hand):
    if match_all(enumerate(hand.values), lambda x: x[1]+x[0] == hand.values[0]):
        return [5] + hand.values

def flush(hand):
    if len(hand.suits) == 1:
        return [6] + hand.values

def full_house(hand):
    if three_of_a_kind(hand) and one_pair(hand):
        return [7] + hand.count_value[3] + hand.count_value[2]

def four_of_a_kind(hand):
    if 4 in hand.count_value:
        return [8] + hand.count_value[4] + hand.values

def straight_flush(hand):
    if flush(hand) and straight(hand):
        return [9] + hand.values

def royal_flush(hand):
    if straight_flush(hand) and hand.values[0] == 14:
        return [10] + hand.values

assert royal_flush(Hand('JD AD KD QD TD'))
assert not royal_flush(Hand('JS AD KD QD TD'))
assert not royal_flush(Hand('7D AD KD QD TD'))
assert straight_flush(Hand('JD 9D KD QD TD'))
assert not straight_flush(Hand('JD 9D KD QD TS'))
assert four_of_a_kind(Hand('6D 6C 6H 6S 9H'))
assert four_of_a_kind(Hand('3D 6D 6C 6H 6S'))
assert not four_of_a_kind(Hand('3D 3C 6C 6H 6S'))
assert full_house(Hand('3H 3D 7C 7H 7S'))
assert flush(Hand('8C 7C 5C 9C TC'))
assert straight(Hand('3C 4S 5C 6S 7C'))
assert three_of_a_kind(Hand('8C 7S 8D 3S 8S'))
assert two_pairs(Hand('3C 8C 3S 8S 9D'))


ranks = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair, high_card]


def rank_hand(hand):
    for rank in ranks:
        r = rank(hand)
        if r:
            return r


def play(h1, h2):
    return rank_hand(h1) > rank_hand(h2)


def test_play():
    hands = """5H 5C 6S 7S KD 2C 3S 8S 8D TD
               5D 8C 9S JS AC 2C 5C 7D 8S QH
               2D 9C AS AH AC 3D 6D 7D TD QD
               4D 6S 9H QH QC 3D 6D 7H QD QS
               2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"""
    for line in hands.split('\n'):
        line = line.strip()
        h1, h2 = Hand(line[:14]), Hand(line[15:])
        yield play(h1, h2)


assert list(test_play()) == [False, True, False, True, True]


def solve_problem():
    f = open('poker.txt')
    x = 0
    for line in f:
        h1, h2 = Hand(line[:14]), Hand(line[15:])
        if play(h1, h2):
            x += 1
    f.close()
    print x

solve_problem()