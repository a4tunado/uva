import sys

while True:
    l = sys.stdin.readline()
    if not l:
        break

    n = int(l)
    names = sys.stdin.readline().split()
    debit, credit = dict(), dict()
    while n != 0:
        n -= 1
        v = sys.stdin.readline().split()
        d = int(v[1])
        k = int(v[2])
        c = d // k if k != 0 else 0
        credit[v[0]] = credit.get(v[0], 0) - c * k
        for e in v[3:]:
            credit[e] = credit.get(e, 0) + c
    
    for e in names:
        print('%s %s' % (e, credit[e]))
