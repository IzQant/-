import sys

def foursquares(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        mini = sys.maxsize
        for j in range(1, int(i**0.5)+1):
            mini = min(mini, dp[i-j*j])
        dp[i] = mini + 1
    return dp[n]

n = int(sys.stdin.readline())
print(foursquares(n))
