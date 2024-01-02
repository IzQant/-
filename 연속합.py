input = __import__('sys').stdin.readline

n = int(input())

A = list(map(int, input().split()))
dp = []
dp.append(A[0])

for i in range(1, n):
    dp.append(max(A[i], dp[i-1]+A[i]))
print(max(dp))