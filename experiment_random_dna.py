import sys
import timeit
from assembler import DNAAssembler
from sampler import random_dna_string, random_reads


"""
CAAATGCATCAT
TCATCAAATGCA

CAAATGCATCATCAAATGCATCAT
            CAAATGCATCAT
           TCAAATGCATCA
          ATCAAATGCATC
         CATCAAATGCAT
        TCATCAAATGCA
       ATCATCAAATGC
        TCATCAAATGCA
"""

def are_rotation(line1, line2):
    if len(line1) != len(line2):
        return False
    return line1 in (line2 + line2)


def run_random_assembly(dnalen, nreads, readlen, k, seed=31):
    dna = random_dna_string(dnalen, seed=seed)
    reads = random_reads(dna, nreads, readlen, seed=seed)
    dnaa = DNAAssembler(k)
    result = dnaa(reads)
    print(f'{len(dnaa.g.nodes)} nodes')
    print(f'{len(dnaa.g.edges)} edges')
    dnaa.g.dump()
    return dna, result, are_rotation(dna, result)


def main():
    assert len(sys.argv) == 5
    dnalen, nreads, readlen, k = map(int, sys.argv[1:])
    for seed in range(1):
        dna, result, status = run_random_assembly(dnalen, nreads, readlen, k, seed=seed)
        print(dna)
        print(result)
        print(status)


if __name__ == '__main__':
    main()
