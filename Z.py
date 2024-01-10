input = __import__('sys').stdin.readline
N, r, c = map(int, input().split())
cnt = 0
#순서는 2-1-3-4
while N > 1:
    sz = 2**N // 2
    if r < sz and c < sz: #2사분면
        pass
    elif r < sz and c >= sz: #1사분면
        cnt += sz ** 2 #2사분면에서 1사분면으로 이동
        c -= sz
    elif r >= sz and c < sz: #3사분면
        cnt += sz ** 2 * 2 #2사분면에서 3사분면으로 이동
        r -= sz
    elif r >= sz and c >= sz: #4사분면
        cnt += sz ** 2 * 3 #2사분면에서 4사분면으로 이동
        r -= sz
        c -= sz
    N -= 1 #배열 크기 반으로 줄이기

if r == 0 and c == 0: #2사분면
    print(cnt)
elif r == 0 and c == 1: #1사분면
    print(cnt + 1)
elif r == 1 and c == 0: #3사분면 
    print(cnt + 2)
elif r == 1 and c == 1: #4사분면
    print(cnt + 3)
