input = __import__('sys').stdin.readline
dp = [0]*1001
dp[0] = 1
dp[1] = 3
dp[2] = 5
dp[3] = 11
n = int(input())
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[n-1]%10007)