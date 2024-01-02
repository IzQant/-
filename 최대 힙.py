from queue import PriorityQueue
input = __import__('sys').stdin.readline

que = PriorityQueue()
N = int(input()) #연산 개수
for i in range(N):
    x = int(input())
    if x == 0:
        if que.empty() == True:
            print(0)
        else:
            print(que.get()[1])
    else:
        que.put(((-1)*x, x))