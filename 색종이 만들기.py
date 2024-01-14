import sys
input = __import__('sys').stdin.readline
sys.setrecursionlimit(10**7)
#분할 정복
N = int(input()) #한 변의 길이
#정사각형이므로 행, 열 둘다 N
board = [list(map(int, input().split())) for _ in range(N)]
cw = 0
cb = 0
def solve(x, y, N):
    global cw, cb
    cp = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if board[i][j] == 1:
                cp += 1
    if cp == 0:
        cw += 1
    elif cp == N**2:
        cb += 1
    else:
        solve(x, y, N//2)
        solve(x, y + N//2, N//2)
        solve(x + N//2, y, N//2)
        solve(x + N//2, y + N//2, N//2)
    return

solve(0, 0, N)
print(cw)
print(cb)