input = __import__('sys').stdin.readline
n = int(input()) #컴퓨터의 수
num = int(input()) #컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]
for _ in range(num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, visited = []): #깊이우선탐색
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            visited = dfs(i, visited)
    return visited

print(len(dfs(1))-1)