import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    lst.append((age, name))
lst.sort(key = lambda x: x[0])
for x,y in lst:
    print(x,y)