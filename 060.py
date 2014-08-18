"""
Project Euler Problem #60
==========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""


from utils import PrimeSieve, is_prime, to_digits, from_digits
from itertools import combinations


def concat(n1, n2):
    return from_digits(to_digits(n1) + to_digits(n2))


def are_concats_prime(p1, p2, sieve):
    return is_prime(concat(p1, p2), sieve) and is_prime(concat(p2, p1), sieve)


def remove_from_graph(graph, node):
    for edge in graph[node]:
        graph[edge].remove(node)
    del graph[node]


def remove_unconnected_nodes(graph, min_connectivity):
    # remove all nodes that have connectivity <= length
    to_remove = [node for node in graph if len(graph[node]) < min_connectivity]
    if to_remove:
        for node in to_remove:
            remove_from_graph(graph, node)
        return remove_unconnected_nodes(graph, min_connectivity)


def is_clique(graph, nodes):
    for i in xrange(len(nodes)):
        node = nodes[i]
        edges = graph[node]
        for j in xrange(i+1, len(nodes)):
            if not nodes[j] in edges:
                return False
    return True


def find_max_clique(graph, length):
    # remove all nodes that have connectivity <= length
    remove_unconnected_nodes(graph, length-1)
    while graph:
        node = graph.keys()[0]
        edges = graph[node]
        for combo in combinations(edges, length-1):
            clique = list(combo) + [node]
            if is_clique(graph, clique):
                return clique
        remove_from_graph(graph, node)
        remove_unconnected_nodes(graph, length-1)


def construct_graph(size):
    sieve = PrimeSieve(size)
    sieve2 = PrimeSieve(concat(size, size)**.8+1)
    print 'sieves constructed'
    graph = {}
    count = 0
    for p1 in sieve:
        count += 1
        if count % 128 == 0: print p1
        graph[p1] = set()
        for p2 in graph:
            if p1 != p2 and are_concats_prime(p1, p2, sieve2):
                graph[p1].add(p2)
                graph[p2].add(p1)
    return graph


def solve():
    graph = construct_graph(10000)
    print 'graph constructed'
    print find_max_clique(graph, 5)



# solve()
# answer: [5701, 5197, 8389, 6733, 13]
print sum([5701, 5197, 8389, 6733, 13])




