import sys
N, M = map(int, sys.stdin.readline().split())
H = set(sys.stdin.readline().strip() for _ in range(N))
S = set(sys.stdin.readline().strip() for _ in range(M))
HS = H & S
print(len(HS))
for i in sorted(HS):
    print(i)