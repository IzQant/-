import sys
N = int(sys.stdin.readline().strip())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
ML = list(map(int, sys.stdin.readline().split()))
for i in ML:
    print(1) if i in A else print(0)
#단순 비교할때는 list보다 set 사용!