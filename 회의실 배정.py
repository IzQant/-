import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst.sort(key = lambda x : (x[1], x[0]))

S = 0
E = 0
for a, b in lst:
    if a >= E:
        S += 1
        E = b
print(S)