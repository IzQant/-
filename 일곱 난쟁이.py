from itertools import *
input = __import__('sys').stdin.readline

people = [int(input()) for _ in range(9)]
P = list(permutations(people, 7))
for i in P:
    if sum(i) == 100:
        for j in sorted(list(i)):
            print(j)
        break