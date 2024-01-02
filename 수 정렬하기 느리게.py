import sys
N = int(input())
lst = []
for i in range(N):
    n = int(sys.stdin.readline())
    lst.append(n)
lst.sort()
for j in lst:
    print(j)
