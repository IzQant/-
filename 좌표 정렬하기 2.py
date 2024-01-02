import sys
N = int(sys.stdin.readline())
list1 = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    list1.append([y, x])
list2 = sorted(list1)
for y,x in list2:
    print(x, y)