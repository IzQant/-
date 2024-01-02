#어렵다
input = __import__('sys').stdin.readline

N = int(input())
stairs = [0]*301
scores = [0]*301
for i in range(N):
    scores[i] = int(input())

stairs[0] = scores[0]
stairs[1] = scores[1] + scores[0]
stairs[2] = max(scores[2] + scores[1], scores[2] + scores[0])

for i in range(3, N):
    stairs[i] = max(scores[i] + scores[i-1] + stairs[i-3], scores[i] + stairs[i-2])
print(stairs[N-1])