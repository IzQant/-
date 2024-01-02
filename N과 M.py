#1번
input = __import__('sys').stdin.readline
N, M = map(int, input().split())
lst = []
def dfs(S):
    if len(lst) == M:
        print(*map(str, lst))
        return
    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            dfs(S+1)
            lst.pop()
dfs(1)