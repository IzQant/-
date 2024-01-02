import sys
N, K = map(int, sys.stdin.readline().split())
coin = list(sys.stdin.readline().strip() for _ in range(N))
coin.reverse()
cnt = 0
for i in range(N):
    if K - int(coin[i]) >= 0:
        cnt += K // int(coin[i])
        K = K % int(coin[i])
    if K == 0:
        break
print(cnt)
