import sys
def check(mid):
    cnt  = 0
    for i in line:
        cnt += i // mid
    return cnt >= N

K, N = map(int, sys.stdin.readline().split())

line = [int(sys.stdin.readline()) for _ in range(K)]

left = 0
right = max(line) + 1

while left + 1 < right:
    mid = (left+right)//2

    if check(mid):
        left = mid
    else:
        right = mid

print(left)