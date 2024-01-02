import sys
import math
N = int(input())
c = 0
lst = list(map(int, sys.stdin.readline().split()))
for i in range(0, N):
    if lst[i] == 1:
        continue
    prime = True
    for j in range(2, int(lst[i]**0.5)+1):
        if lst[i]%j == 0:
            prime = False
            break
    if prime:
        c += 1
print(c)


