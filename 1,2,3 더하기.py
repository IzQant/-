#나는 dp가 싫어요
input = __import__('sys').stdin.readline
T = int(input())
cases = [int(input()) for _ in range(T)]
dp = [0]*11
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
for i in cases:
    print(dp[i])