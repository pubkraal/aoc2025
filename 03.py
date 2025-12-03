import sys


def fn(lc, num=12):
    if len(lc) == num:
        return lc

    s = lc
    if num > 1:
        s = lc[: -(num - 1)]
    h = s.index(max(s))
    m = s[h]

    if num > 1:
        hn = h + 1
        m += fn(lc[hn:], num - 1)

    return m


def calc(lc):
    return int(fn(lc, 2))


def calcp2(lc):
    return int(fn(lc, 12))


if __name__ == "__main__":
    p1 = 0
    p2 = 0

    source = sys.argv[1] if len(sys.argv) > 1 else "03.txt"
    lines = open(source).readlines()

    p1 = sum(map(calc, (line.strip() for line in lines)))
    p2 = sum(map(calcp2, (line.strip() for line in lines)))

    print(p1)
    print(p2)
