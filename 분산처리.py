input = __import__('sys').stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(10 if pow(a,b,10) == 0 else pow(a,b,10))