import sys

while True:
    h, u, d, f = map(int, sys.stdin.readline().split())
    if h == 0:
        break
    c, a, i = 0, 0, 0
    f = 1e-2 * f * u
    while True:
        i += 1
        c += max(0, u - a)
        if c > h:
            print('success on day %d' % i)
            break
        c -= d
        if c < 0:
            print('failure on day %d' % i)
            break
        a += f
