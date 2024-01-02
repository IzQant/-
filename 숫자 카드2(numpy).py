import sys
import numpy as np
N = int(sys.stdin.readline())
A = np.array(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = np.array(list(map(int, sys.stdin.readline().split())))
result = np.zeros(M)
for i in range(0, N):
    if A[i] in B:
        R = np.where(A[i] == B)
        result[R] += 1
R = result.tolist()
R = list(map(int, R))
print(*R)