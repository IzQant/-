from collections import deque
input = __import__('sys').stdin.readline
 
n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * (m) for _ in range(n)]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newx = dx[i] + x
            newy = dy[i] + y

            if 0 <= newx < n and 0 <= newy < m and visited[newx][newy] == -1:
                if board[newx][newy] == 0:
                    visited[newx][newy] = 0
                elif board[newx][newy] == 1:
                    visited[newx][newy] = visited[x][y] + 1
                    queue.append((newx, newy))

for i in range(n):
    for j in range(m):
        if board[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
