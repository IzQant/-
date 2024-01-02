#BFS가 나을듯
input = __import__('sys').stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    global w, B
    queue = deque()
    queue.append((a, b))
    w = 0
    B = 0
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if graph[nx][ny] == graph[a][b] and graph[a][b] == 'w':
                w += 1
            elif graph[nx][ny] == graph[a][b] and graph[a][b] == 'b':
                B += 1
    return
        

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    str = input().rstrip()
    lst = list(str)
    for j in lst:
        graph[i+1].append(j)


print(w**2, B**2, sep="")

#장군님이 dfs로 하시란다!

