""" Data structure and algorithm for finding Eulerian cycle in a directed graph """

import itertools
import random

DEBUG = False


class Graph:
    """ Directed Graph """
    def __init__(self):
        self.edges = {}
        self.nodes = set()
        self.adj = {}

    def add_node(self, n):
        if n in self.nodes:
            return

        self.nodes.add(n)
        self.adj[n] = []

    def add_edge(self, s, t):
        self.add_node(s)
        self.add_node(t)
        self.edges[(s, t)] = self.edges.get((s, t), 0) + 1
        self.adj[s].append(t)
    
    def dump(self):
        for n in self.nodes:
            print(f'{n} -> {", ".join(self.adj[n])}')


def eulerian_cycle(gr: Graph):
    """ Finds eulerian cycle """
    start = random.choice(list(gr.nodes))
    if DEBUG:
        print(f'start {start}')
    visited_edges = dict()
    cycle = []
    stack = [start]

    while len(stack) > 0:
        current_node = stack[-1]

        for neib in gr.adj[current_node]:
            current_edge = (current_node, neib)
            graph_edge_count = gr.edges[current_edge]
            current_edge_count = visited_edges.get(current_edge, 0)
            if current_edge_count < graph_edge_count:
                visited_edges[current_edge] = current_edge_count + 1
                stack.append(neib)
                break
        else:
            cycle.append(stack.pop())

    return cycle[::-1][:-1]

# TODO
#
# def eulerian_path(gr, rng):
#     source, target = None, None
#     for idx, (adj, inc) in enumerate(zip(gr.adj, gr.incident)):
#         if len(adj) > len(inc):
#             source = gr.nodes[idx]
#             source_idx = idx
#         elif len(adj) < len(inc):
#             target = gr.nodes[idx]
#             target_idx = idx
#         if source is not None and target is not None:
#             break

#     if source is not None and target is not None:
#         gr.add_edge(target, source)

#     cycle = eulerian_cycle(gr, rng=rng)
#     if cycle[0] != source_idx or cycle[-1] != target_idx:
#         for idx, item in enumerate(cycle):
#             if item == target_idx and idx+1 != len(cycle) and cycle[idx+1] == source_idx:
#                 cycle = cycle[idx + 1:] + cycle[1:idx + 1]
#     return [gr.nodes[idx] for idx in cycle]


def main():
    gr = Graph()

    for kmer in itertools.product('01', repeat=8):
        line = ''.join(kmer)
        if DEBUG:
            print(f'{kmer} -> {line}')
        gr.add_edge(line[:-1], line[1:])

    print(len(gr.nodes))
    cyc = eulerian_cycle(gr)
    if DEBUG:
        print(cyc)
    unistr = ''.join([item[-1] for item in cyc])
    print(len(unistr))
    print(unistr)


if __name__ == '__main__':
    main()
