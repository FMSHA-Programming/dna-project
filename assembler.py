from euler import Graph, eulerian_cycle


class DNAAssembler:
    def __init__(self, k):
        self.k = k
        self.g = Graph()
        
    def add_kmer(self, kmer):
        self.g.add_edge(kmer[:-1], kmer[1:])
    
    def add_read(self, read):
        assert len(read) > self.k
        for i in range(len(read) - self.k):
            self.add_kmer(read[i:i + self.k])
    
    def __call__(self, reads):
        for r in reads:
            self.add_read(r)
        cyc = eulerian_cycle(self.g)
        print(f'{len(cyc)} cycle')
        return ''.join([item[-1] for item in cyc])
