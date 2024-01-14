import sys
input = __import__('sys').stdin.readline

n, m = map(int, input().split()) #n = 세로, m = 가로
board = [list(map(int, input().split())) for _ in range(n)]
dp = [ [0 for _ in range(m)] for _ in range(n)]

def solve(board, dp, n, m):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 0
    for i in range(0, n): 
        for j in range(0, m):
            if board[i][j] == 2:
                dp[i][j] = 0
                cnt = 0
                where2i = i
                where2j = j

            elif board[i][j] == 1:
                if i > 0 and j > 0:
                    if dp[i][j-1] == 0 or dp[i-1][j] == 0:
                        cnt = max(dp[i][j-1], dp[i-1][j])
                    elif dp[i][j] < dp[i-1][j]:
                        dp[i][j] = dp[i-1][j] + 1
                        for a in range(j, 0, -1):
                            if dp[i][a-1] < dp[i][a] and dp[i-1][a-1] == 0:
                                if board[i][a-1] == 0:
                                    continue
                                dp[i][a-1] = dp[i][a] + 1
                                
                            
                        continue
                    else:
                        cnt = min(dp[i][j-1], dp[i-1][j])
                    
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + 1
                    continue
                cnt += 1
                dp[i][j] += cnt
    hm0 = 0
    for i in range(4):
        newX = where2i + dx[i]
        newY = where2j + dy[i]
        if board[newX][newY] == 0:
            hm0 += 1
        if where2i == 0 or where2j == 0:
            if hm0 == 2:
                for i in range(n):
                    for j in range(m):
                        if i == where2i or j == where2j:
                            dp[i][j] = 0
                            dp[i][j] = 0
                            continue
                        if dp[i][j] == 0:
                            continue
                        dp[i][j] = -1
        elif hm0 == 4:
            for i in range(n):
                    for j in range(m):
                        if i == where2i or j == where2j:
                            dp[i][j] = 0
                            dp[i][j] = 0
                            continue
                        if dp[i][j] == 0:
                            continue
                        dp[i][j] = -1
    return
solve(board, dp, n, m)
for k in dp:
    print(*k)





