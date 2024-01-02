import sys

def check(mid):
    cnt = 1
    current = min(house)
    for i in house:
        if i - current >= mid:
            cnt += 1
            current = i
    return cnt >= C

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()
left = 0

right = max(house) - min(house) + 1#거리

while left + 1 < right:
    current = min(house)
    mid = (left+right) // 2
    
    if check(mid):
        left = mid 
    else:
        right = mid

print(left)

