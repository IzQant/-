#5번
input = __import__('sys').stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
dp = []
visited = [0]*N
depth = 0

def solve(depth, N, M):
    if depth == M:
        print(*map(str, dp))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dp.append(A[i])
            solve(depth+1, N, M)
            dp.pop()
            visited[i] = 0
solve(0, N, M)