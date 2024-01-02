from sys import stdin
N = int(input())
L = [0]*10001
for i in range(N):
    n = int(stdin.readline())
    L[n] += 1
for j in range(10001):
    if L[j] != 0:
        for v in range(L[j]):
            print(j)
