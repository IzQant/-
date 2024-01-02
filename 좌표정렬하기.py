from sys import stdin
N = int(stdin.readline())
lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(key = lambda x : (x[0], x[1]))
for a, b in lst:
    print(a, b)



