import sys
N = int(sys.stdin.readline())
stu = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    stu.append((x, y))
for j in stu:
    rank = 1
    for v in stu:
        if j[0] < v[0] and j[1] < v[1]:
            rank += 1
    print(rank, end=" ")