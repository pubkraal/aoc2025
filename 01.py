import sys

source = sys.argv[1] if len(sys.argv) > 1 else "01.txt"

lines = open(source).readlines()

pos = 50
t = 0
t2 = 0

for line in lines:
    n = int(line[1:])

    op = lambda x: (x + 1) % 100
    if line[0] == "L":
        op = lambda x: (x - 1) % 100

    for _ in range(n):
        pos = op(pos)
        if pos == 0:
            t2 += 1
    if pos == 0:
        t += 1

print(t)
print(t2)
