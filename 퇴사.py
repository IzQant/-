input = __import__('sys').stdin.readline

N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]
