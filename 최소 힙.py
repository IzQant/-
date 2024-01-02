from queue import PriorityQueue
input = __import__('sys').stdin.readline
#정렬된 큐 -- 우선순위 큐(가장 작은 값 뽑기)
N = int(input())

que = PriorityQueue(maxsize = N)

for _ in range(N):
    x = int(input())
    if x > 0:
        que.put(x)
    if x == 0:
        if que.empty():
            print(0)
        else:
            print(que.get())
            