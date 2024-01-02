input = __import__('sys').stdin.readline

numbers = list(int(input()) for _ in range(7))
cnt = 0
mini = max(numbers)
for i in numbers:
    if i % 2 != 0:
        cnt += i
        if i < mini:
            mini = i
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(mini)