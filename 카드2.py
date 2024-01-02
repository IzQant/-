import sys
from collections import deque
N = int(sys.stdin.readline())
que = deque()
def top():
    for i in range(1, N+1):
        que.append(i)
    while que:
        if len(que) > 1:
            que.popleft()
            que.append(que.popleft())
        else:
            break
    print(que[0])
top()

