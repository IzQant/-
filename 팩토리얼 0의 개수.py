import sys
N = int(sys.stdin.readline())

factorial = 1
cnt = 0

for i in range(0, N-1):
    factorial = factorial * (N-i)
factorial = list(str(factorial)[::-1])

for j in range(0, len(factorial)):
    if factorial[j] == '0':
        cnt += 1
        if factorial[j+1] != '0':
            break
print(cnt)
