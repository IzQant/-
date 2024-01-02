#쫄지말기
input = __import__('sys').stdin.readline
N = int(input()) #수열 크기
A = list(map(int, input().split())) #수열
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))