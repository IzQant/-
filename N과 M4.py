#4번
input = __import__('sys').stdin.readline
N, M = map(int, input().split())

lst = []
def dfs(S, index):
    if len(lst) == M:
        print(*map(str, lst))
        return
    for i in range(index, N+1):
        lst.append(i)
        dfs(S+1, i) #다음부터는 i보다 큰 수만 선택 가능
        lst.pop()
dfs(1, 1)