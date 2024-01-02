import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
left = 1
right = max(tree)
while left <= right:
    mid = (left+right)//2

    cnt = 0#나무
    
    for i in tree:
        if i >= mid:
            cnt += i - mid #얻을 수 있는 나무 길이

    if cnt >= M:
        left = mid + 1 #mid값 이상의 길이로 자르기
    else:
        right = mid - 1 #mid값 이하의 길이로 자르기

print(right)