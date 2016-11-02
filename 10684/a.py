import sys

n = int(sys.stdin.readline())
while n:
    b = list(map(int, sys.stdin.readline().split()))
    s = [0] * n
    s[0] = b[0]
    for i, e in enumerate(b[1:]):
        s[i + 1] = s[i] + e

    max_seq = b[0]
    for i in range(n-1):
        for j in range(i+1, n):
            max_seq = max(max_seq, s[j] - s[i])

    if max_seq < 0:
        print('Losing streak.')
    else:
        print('The maximum winning streak is %s.' % max_seq)
    
    n = int(sys.stdin.readline())
