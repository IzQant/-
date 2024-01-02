input = __import__('sys').stdin.readline
N = int(input())
room = list(range(1, 100))
L = []
for i in range(N):
    k = int(input())
    n = int(input())
    for j in range(k):
        for v in range(1, len(room)):
            room[v] = room[v-1] + room[v]
    L.append(room[n-1])
    room = list(range(1, 100))
for s in range(len(L)):
    print(L[s])