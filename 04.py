import sys
import copy

source = sys.argv[1] if len(sys.argv) > 1 else "04_test.txt"
lines = open(source).readlines()
grid = [[c for c in line.strip()] for line in lines]


def get_adj(grid, r, c):
    muts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjs = []
    maxr = len(grid) - 1
    maxc = len(grid[0]) - 1
    for m in muts:
        nr = r + m[0]
        nc = c + m[1]
        if 0 <= nr <= maxr and 0 <= nc <= maxc:
            adjs.append(grid[nr][nc])
    return adjs


p1 = 0
p2 = 0
loop = 0

while True:
    p2grid = copy.deepcopy(grid)
    changed = False

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != "@":
                continue

            adj = get_adj(grid, r, c)
            if sum(a == "@" for a in adj) < 4:
                p1 += 1
                p2 += 1
                p2grid[r][c] = "."
                changed = True

    if loop == 0:
        print(p1)

    if not changed:
        break

    grid = copy.deepcopy(p2grid)
    loop += 1

print(p2)
