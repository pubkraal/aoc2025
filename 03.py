import sys
from multiprocessing import Pool
from itertools import combinations


def fn(lc, num=12):
    if len(lc) == num:
        return lc

    s = lc
    if num > 1:
        s = lc[: -(num - 1)]
    h = s.index(max(s))
    m = s[h]

    if num > 1:
        m += fn(lc[h + 1 :], num - 1)

    return m


def calcp2(lc):
    m = fn(lc)
    return int(m)


if __name__ == "__main__":
    p1 = 0
    p2 = 0

    source = sys.argv[1] if len(sys.argv) > 1 else "03.txt"
    lines = open(source).readlines()

    with Pool(None) as p:
        p2 = sum(p.map(calcp2, (l.strip() for l in lines)))

    # sum of maximum of 2 digits per line
    for line in lines:
        lc = line.strip()
        m = max(int("".join(x)) for x in combinations(lc, 2))
        p1 += m

    print(p1)
    print(p2)
