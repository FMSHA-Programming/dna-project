import itertools
import random


class Graph:
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


def eulerian_cycle(gr: Graph):
    start = random.choice(list(gr.nodes))
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

    return cycle[::-1]


def main():
    gr = Graph()

    for kmer in itertools.product('01', repeat=3):
        line = ''.join(kmer)
        print(f'{kmer} -> {line}')
        gr.add_edge(line[:-1], line[1:])

    print(len(gr.nodes))
    cyc = eulerian_cycle(gr)
    print(cyc)


if __name__ == '__main__':
    main()
