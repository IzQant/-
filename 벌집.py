input = __import__('sys').stdin.readline

N = int(input())
current = 1
i = 1
while True:
    if current >= N:
        print(i)
        break
    else:
        current += 6*i
        i += 1