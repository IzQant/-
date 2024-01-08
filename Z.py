input = __import__('sys').stdin.readline
N, r, c = map(int, input().split())
sz = 2 ** N
board = [ [0 for _ in range(sz)] for _ in range(sz)]

index = 0

def solve(x, y, sz):
    global index
    if (sz == 1):
        board[x][y] = index
        index += 1
        return
    sz //= 2
    if r < x + sz and c < y + sz:
        solve(x, y, sz)
    elif r < x + sz and c >= y + sz:
        index += sz * sz
        solve(x, y + sz, sz)
    elif r >= x + sz and c < y + sz:
        index += 2 * sz * sz
        solve(x + sz, y, sz)
    elif r >= x + sz and c >= y + sz:
        index += 3 * sz * sz
        solve(x + sz, y + sz, sz)

solve(0, 0, sz)
print(board[r][c])
