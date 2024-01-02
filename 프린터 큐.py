import sys
lst = []
n = int(sys.stdin.readline())
for _ in range(n):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    idx = list(range(N))
    idx[M] = 'target'
    order = 0
    while True:
        if lst[0] == max(lst):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                lst.pop(0)
                idx.pop(0)
        else:
            lst.append(lst.pop(0))
            idx.append(idx.pop(0))

