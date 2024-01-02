import sys
from itertools import accumulate
N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
result = list(accumulate(time))
print(sum(result))