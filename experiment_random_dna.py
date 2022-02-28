import sys
import timeit
from assembler import DNAAssembler
from sampler import random_dna_string, random_reads


def are_rotation(line1, line2):
    if len(line1) != len(line2):
        return False
    return line1 in (line2 + line2)


def run_random_assembly(dnalen, nreads, readlen, k, cycle, rng):
    dna = random_dna_string(dnalen, rng)
    reads = random_reads(dna, nreads, cycle, readlen, rng)
    dnaa = DNAAssembler(k, cycle, rng)
    result = dnaa(reads)
    print(f'{len(dnaa.g.nodes)} nodes')
    print(f'{len(dnaa.g.edges)} edges')
    dnaa.g.dump()
    if cycle:
        status = are_rotation(dna, result)
    else:
        status = dna == result
    return dna, result, status


def main():
    assert len(sys.argv) == 7
    dnalen, nreads, readlen, k, seed, ntry = map(int, sys.argv[1:])
    rng = np.random.default_rng(seed=seed)
    nsuccess = 0
    for idx in range(ntry):
        dna, result, status = run_random_assembly(dnalen, nreads, readlen, k, rng)
        print(dna)
        print(result)
        if status:
            nsuccess += 1
        print(status)
    print(f'Success rate: {nsuccess}/{ntry}')


if __name__ == '__main__':
    main()
