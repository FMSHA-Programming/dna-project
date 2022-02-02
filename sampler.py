import numpy as np


def random_dna_string(size, seed=31):
    nucl = list('ATCG')
    rng = np.random.default_rng(seed=seed)
    return ''.join(rng.choice(nucl, size=size))


def random_reads(dna, size, length=200, seed=31):
    """[summary]

    Args:
        dna ([type]): [description]
        size ([type]): [description]
        length (int, optional): [description]. Defaults to 200.
        seed (int, optional): [description]. Defaults to 31.

    Returns:
        [type]: [description]
    """
    assert len(dna) > length
    dna1 = dna + dna[:length]
    rng = np.random.default_rng(seed=seed)
    return [dna1[i:i+length] for i in rng.integers(0, len(dna), size=size)]


if __name__ == '__main__':
    dna = random_dna_string(189)
    print('\n'.join(random_reads(dna, 35, 15)))
