import sys
input = __import__('sys').stdin.readline
sys.setrecursionlimit(10**6)
def dfs(S):
    visited.append(S)
    for i in graph[S]:
        if i not in visited:
            dfs(i)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = []
count = 0
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in range(1, N+1):
    if j not in visited:
        dfs(j)
        count += 1

print(count)