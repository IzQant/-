#파이썬이라서 당했다네요
input = __import__('sys').stdin.readline
from collections import deque

def bfs(graph, node, visited):
    cnt = 1
    queue = deque([node])
    
    visited = [False for _ in range(N+1)]
    visited[node] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)

C = 1
answer = set()
visited = [False for _ in range(N+1)]

for i in range(1, N+1):
    Cnt = bfs(graph, i, visited)
    if Cnt > C:
        C = Cnt
        answer.clear()
        answer.add(i)
        
    elif Cnt == C:
        answer.add(i)
print(*answer)