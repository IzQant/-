N = int(input())
answer = []
for i in range(1, N+1):
    sum = 0
    i = str(i)
    sum += int(i)
    for j in i:
        sum += int(j)
    if sum == N:
        answer.append(i)
        break
if answer:
    print(answer[0])
else:
    print(0)