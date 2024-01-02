input = __import__('sys').stdin.readline
import heapq

def MAX(min_heap):
    global max_heap
    reverse = lambda x: x * -1
    max_heap = list(map(reverse, min_heap))
    heapq.heapify(max_heap)
    max_heap = list(map(reverse, max_heap))
    return max_heap

def MIN(max_heap):
    global min_heap
    reverse = lambda x: x*-1
    min_heap = list(map(reverse, max_heap))
    min_heap = list(map(reverse, min_heap))
    return min_heap

T = int(input())
for _ in range(T):
    N = int(input())
    min_heap = []
    for i in range(N):
        X, y = map(str, input().split())
        if X == 'I':
            heapq.heappush(min_heap, int(y))
            
        if X == 'D' and y == '-1': #최소 힙
            try:
                heapq.heappop(min_heap)
            except:
                continue
        if X == 'D' and y == '1': #최대 힙
            try:
                MAX(min_heap)
                heapq.heappop(max_heap)
                MIN(max_heap)

            except:
                continue
    try:
        print(min_heap[-1], min_heap[0], sep=' ')
    except:
        print('EMPTY')






    