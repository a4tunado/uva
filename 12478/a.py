import sys

NAMES_ORIG = '''RAKIBUL
ANINDYA
MOSHIUR
SHIPLU
KABIR
SUNNY
OBAIDA
WASI
'''

NAMES_ORIG = NAMES_ORIG.split()

NAMES = [sorted(n) for n in NAMES_ORIG]
GRID = [sys.stdin.readline().split() for _ in range(9)]

COUNT = [0] * len(NAMES)

for r in range(9):
    for c in range(9):
        for j, n in enumerate(NAMES):
            if (c + len(n)) > 9:
                continue
            if sorted(GRID[r][c:c + len(n)]) == n:
                COUNT[j] += 1

for c in range(9):
    for r in range(9):
        for j, n in enumerate(NAMES):
            if (r + len(n)) > 9:
                continue
            if sorted(GRID[r + k][c] for k in range(len(n))) == n:
                COUNT[j] += 1

for i, c in enumerate(COUNT):
    if c == 2:
        print(NAMES_ORIG[i])
        break
