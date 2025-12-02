import sys
import re

source = sys.argv[1] if len(sys.argv) > 1 else "02.txt"
sets = open(source).read().strip().split(",")

ranges = []

p1 = 0
p2 = 0

for b in sets:
    x = b.split("-", 2)
    ranges += [list(range(int(x[0]), int(x[1]) + 1))]

for r in ranges:
    for n in r:
        v = "{}".format(n)

        # part 1
        if re.fullmatch(r"^(.+)\1$", v):
            p1 += n

        # part 2
        if re.fullmatch(r"^(.+)\1+$", v):
            p2 += n

print(p1)
print(p2)
