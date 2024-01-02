#BFS로 풀기
input = __import__('sys').stdin.readline
from collections import deque

def bfs(graph,node):
    num = [0] * (N+1)
    queue = deque([node])
    visited[node] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                num[i] = num[v] + 1
                queue.append(i)
                visited[i] = 1

    return sum(num)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

frd = []

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,N+1):
    visited = [0] * (N+1)
    frd.append(bfs(graph, i))

print(frd.index(min(frd))+1)