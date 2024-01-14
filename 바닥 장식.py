from collections import deque
input = __import__('sys').stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def bfs(i, j):
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        if board[x][y] == "-":
            board[x][y] = 1
            if y + 1 < M and board[x][y+1] == "-":
                queue.append((x, y+1))
        elif board[x][y] == "|":
            board[x][y] = 1
            if x + 1 < N and board[x+1][y] == "|":
                queue.append((x+1, y))
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 1:
            bfs(i, j)
            cnt += 1
print(cnt)