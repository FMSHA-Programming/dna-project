import numpy as np

rng = np.random.default_rng(seed=56)

def random_dna_string(size, rng=rng):
    return ''.join(rng.choice(list('ATCG'), size=size))


def random_reads(dna, size, cycle, length=200, rng=rng):
    assert len(dna) > length
    if cycle:
        dna1 = dna + dna[:length]
        maxidx = len(dna)
    else:
        dna1 = dna
        maxidx = len(dna) - length
    return [dna1[i:i+length] for i in rng.integers(0, maxidx, size=size)]


if __name__ == '__main__':
    dna = random_dna_string(189)
    print(dna)
    print('\n'.join(random_reads(dna, 35, cycle=False, length=15)))
