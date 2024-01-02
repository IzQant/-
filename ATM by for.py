import sys
N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
for i in range(1, len(time)):
    time[i] += time[i-1]
print(sum(time))