import sys
n = int(sys.stdin.readline())
L = []
for i in range(1, n+1):
    N = sys.stdin.readline().strip()
    L.append(N)
sL = set(L)
L = list(sL)
L.sort()
L.sort(key = len)
for j in L:
    print(j)
