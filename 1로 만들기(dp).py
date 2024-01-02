input = __import__('sys').stdin.readline
#dp로 해볼까
N = int(input())

dp = [0]*(N+1)
dp[1] = 0

if N == 1:
    print(0)
    exit()
    
dp[2] = 1

if N == 2:
    print(1)
    exit()
for i in range(3, N+1):
    dp[i] = dp[i-1]+1

    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])