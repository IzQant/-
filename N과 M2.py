#백트래킹
#2번
input = __import__('sys').stdin.readline

N, M = map(int, input().split()) #자연수 개수, 고를 수의 개수
lst = []
def dfs(S):
    if len(lst) == M:
        print(*map(str, lst))
        return 
    for i in range(S, N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()
dfs(1)