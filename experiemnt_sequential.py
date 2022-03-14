from assembler import DNAAssembler
import numpy as np
from timeit import repeat, timeit

def get_data(ifname, dnalen, k, rng):
    with open(ifname, 'r') as ifile:
        dna = ifile.readline()[:dnalen]
    reads = [dna[i:i+k] for i in range(dnalen - k + 1)]
    rng.shuffle(reads)
    return dna, reads

def main(dnalen, k):
    rng = np.random.default_rng(seed=78)
    ifname = './data/E_coli.txt'
    dnai, reads = get_data(ifname, dnalen, k, rng)
    adna = DNAAssembler(k, False, rng)
    dnao = adna(reads)
    print(dnai == dnao, end=' ')

def scan_size(k):
    rng = np.random.default_rng(seed=78)
    ifname = './data/E_coli.txt'

    def fcn(dnai):
        adna = DNAAssembler(k, False, rng)
        dnao = adna(reads)
        print(dnai == dnao, end=' ')

    for exp in range(3, 6):
        for ln in [1, 2, 4, 8]:
            dnalen = ln * 10**exp
            dnai, reads = get_data(ifname, dnalen, k, rng)
            time = timeit(lambda: fcn(dnai), number=1)
            print(f'{dnalen:>10}: {time:.6f}')


if __name__ == '__main__':
    # main(800, 11)
    scan_size(171)

# [
# 'GCAACGGGCAA', 'TGCAACGGGCA',
# 'CAACGGGCAAT', 'TCTGACTGCAA',
# 'TTTCATTCTGA', 'CTGCAACGGGC',
# 'AGCTTTTCATT', 'TTTTCATTCTG',
# 'TGACTGCAACG', 'CTGACTGCAAC',
# 'ACTGCAACGGG', 'ATTCTGACTGC',
# 'GCTTTTCATTC', 'CATTCTGACTG',
# 'CTTTTCATTCT', 'TTCATTCTGAC',
# 'TCATTCTGACT', 'GACTGCAACGG',
# 'TTCTGACTGCA', 'AACGGGCAATA'
# AGCTTTTCATTCTGACTGCAACGGGCAATA
