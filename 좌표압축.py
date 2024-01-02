import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
result = list(set(num))
result.sort()

numdict = {}
for i in range(len(result)):
    numdict[result[i]] = i
for i in num:
    print(numdict[i], end=' ')
