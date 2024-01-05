input = __import__('sys').stdin.readline
from collections import deque
M, N = map(int, input().split())
tomatoes = []
for i in range(N):
    toma = list(map(int, input().split()))
    tomatoes.append(toma)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in tomatoes:
    if 0 not in i:
        print(0)
        exit()

queue = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

cnt = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]

        if 0 <= newx < N and 0 <= newy < M and tomatoes[newx][newy] == 0:
            queue.append((newx, newy))
            tomatoes[newx][newy] = tomatoes[x][y] + 1

for i in tomatoes:
    if 0 in i:
        print(-1)
        exit()

cnt = max(map(max, tomatoes)) - 1

print(cnt)
print(tomatoes)