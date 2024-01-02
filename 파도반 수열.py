input = __import__('sys').stdin.readline
T = int(input())
dp = [0]*101
dp[0] = 1 #p(1)
dp[1] = 1 #p(2)
dp[2] = 1 #p(3)

for i in range(3, 101):
    dp[i] = dp[i-3] + dp[i-2]

for _ in range(T):
    N = int(input())
    print(dp[N-1])