import sys
N = int(sys.stdin.readline())
def sugar(N):
    bag = 0
    while N >= 0:
        if N % 5 == 0:
            bag = bag + N//5
            print(bag)
            break
        elif N == 0:
            print(bag)
        elif N < 3:
            print(-1)
            break
        N -= 3
        bag += 1
sugar(N)