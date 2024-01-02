import sys
n = int(sys.stdin.readline())
stack = []
start = 1
result = []
for i in range(n):
    N = int(sys.stdin.readline())
    for j in range(start, N+1):
        stack.append(j)
        result.append("+")
        start += 1
    if N == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
for j in result:
    print(j)