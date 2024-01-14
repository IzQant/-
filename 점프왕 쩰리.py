from collections import deque
input = __import__('sys').stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j, endi, endj):
    queue = deque([(i, j)])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) == (endi, endj):
            print("HaruHaru")
            return
        
        if 0 <= y+1 < N and y + board[x][y] < N and (x, y+board[x][y]) not in visited:
            visited.add((x, y+board[x][y]))
            queue.append((x, y+board[x][y]))

        if 0 <= x+1 < N and x + board[x][y] < N and (x+board[x][y], y) not in visited:
            visited.add((x+board[x][y], y))
            queue.append((x+board[x][y], y))

    print("Hing")

bfs(0, 0, N-1, N-1)