import sys
input = __import__('sys').stdin.readline
N = int(input().strip())
A = sorted(map(int, input().split()))
M = int(input().strip())
B = list(map(int, input().split()))
result = {}
for i in A:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for i in B:
    if i in result:
        print(result[i], end=" ")
    else:
        print(0, end=' ')