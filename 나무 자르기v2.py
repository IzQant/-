#Lower Bound
import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(tree)

while left + 1 < right:
    mid = (left+right)//2

    cnt = 0

    for i in tree:
        if i >= mid:
            cnt += i - mid
    if M > cnt:
        right = mid
    else:
        left = mid
print(left)

#left..................right
#.........left right........