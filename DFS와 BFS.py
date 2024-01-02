input = __import__('sys').stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(V, visited = []): #깊이기반
    visited.append(V)
    for i in sorted(graph[V]):
        if i not in visited:
             visited = DFS(i, visited)
        
    return visited
    
def BFS(V): #넓이기반
    visited = [V]
    que = [V]
    while que:
        V = que.pop(0)
        for i in sorted(graph[V]):
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited

print(*DFS(V), sep=' ')
print(*BFS(V), sep=' ')