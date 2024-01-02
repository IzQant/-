#리스트 최대한 안 쓰기
from itertools import *
N, M = map(int, input().split())
n = map(int, input().split())
l = list(n)
L = list(permutations(l, 3))
result = 0
for i in L:
    a = sum(i)
    if result < a <= M:
        result = a
print(result)