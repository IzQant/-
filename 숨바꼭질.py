input = __import__('sys').stdin.readline
from collections import deque
N, K = map(int, input().split())

graph = [0] * 1000001
def bfs(N, K):
    queue = deque()
    queue.append(N)
    graph[N] = 1
    while queue:
        n = queue.popleft()
        if n == K:
            print(graph[n] - 1)
            return
        for i in (n - 1, n + 1, n * 2):
            if 0 <= i <= 100000 and graph[i] == 0: # 아직 방문을 안했으면
                queue.append(i)
                graph[i] = graph[n] + 1
bfs(N, K)
