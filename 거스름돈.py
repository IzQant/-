#dp로 해보기
input = __import__('sys').stdin.readline

n = int(input())
dp = [0]*(1000000)
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1
dp[6] = 3
dp[7] = 2
dp[8] = 4
dp[9] = 3

for i in range(10, n+1):
    dp[i] = dp[i-5] + 1

print(dp[n])