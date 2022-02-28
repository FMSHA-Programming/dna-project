from euler import Graph, eulerian_cycle, eulerian_path
import numpy as np

class DNAAssembler:
    def __init__(self, k, cycle, rng):
        self.k = k
        self.g = Graph()
        if cycle:
            self.alg = eulerian_cycle
            self.assembler = self.assembly_cycle
        else:
            self.alg = eulerian_path
            self.assembler = self.assembly_path
        self.rng = rng

    def add_kmer(self, kmer):
        self.g.add_edge(kmer[:-1], kmer[1:])

    def add_read(self, read):
        assert len(read) >= self.k
        for i in range(len(read) - self.k + 1):
            self.add_kmer(read[i:i + self.k + 1])

    def assembly_cycle(self, cyc):
        return ''.join([item[-1] for item in cyc])
    
    def assembly_path(self, path):
        return path[0] + ''.join([item[-1] for item in path[1:]])

    def __call__(self, reads):
        for r in reads:
            self.add_read(r)
        cyc = self.alg(self.g, self.rng)
        print(f'{len(cyc)} cycle')
        return self.assembler(cyc)


def main():
    rng = np.random.default_rng(seed=64)
    reads = [
        'AAAT', 'AATG', 'ACCC', 'ACGC', 'ATAC',
        'ATCA', 'ATGC', 'CAAA', 'CACC', 'CATA',
        'CATC', 'CCAG', 'CCCA', 'CGCT', 'CTCA',
        'GCAT', 'GCTC', 'TACG', 'TCAC', 'TCAT',
        'TGCA',
    ]  # CAAATGCATCATACGCTCACCCAG
       # CAAATGCATCATACGCTCACCCAG
       # CAAATGCATACGCTCATCACCCAG

    dnaa = DNAAssembler(k=4, cycle=False, rng=rng)
    dna = dnaa(reads)
    print(dna)


if __name__ == '__main__':
    main()
