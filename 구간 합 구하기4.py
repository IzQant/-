input = __import__('sys').stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = [0]*100001
result[0] = lst[0]
for v in range(1, N):
    result[v] = lst[v] + result[v-1]
for _ in range(M):
    i, j = map(int, input().split())
    print(result[j-1] - result[i-2])