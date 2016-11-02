import sys

i = 0
while True:
    i += 1
    n, p = map(int, sys.stdin.readline().split())
    if n == 0:
        break
    for _ in range(n):
        sys.stdin.readline()
    best_prop, best_price, best_comp = '', 0, -1
    for _ in range(p):
        prop = sys.stdin.readline().strip()
        price, comp = map(float, sys.stdin.readline().split())
        for _ in range(int(comp)):
            sys.stdin.readline()
        if comp > best_comp or (comp == best_comp and price < best_price):
            best_prop = prop
            best_price = price
            best_comp = comp
    if i != 1:
        print('')
    print('RFP #%d' % i)
    print('%s' % best_prop)
