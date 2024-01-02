input = __import__('sys').stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if land[nx][ny] == 1:
                queue.append((nx, ny))
                land[nx][ny] = 0
    return
                
T = int(input()) #테스트 케이스 개수

for _ in range(T):
    
    M, N, K = map(int, input().split())
    land = [[0]*(M) for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)