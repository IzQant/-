input = __import__('sys').stdin.readline

N = int(input())#색종이 수

board = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y-1, y+9):
        for j in range(x-1, x+9):
            if board[j][i] == 0:
                board[j][i] = 1
                cnt += 1           
print(cnt)