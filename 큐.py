import sys
from collections import deque
que = deque()
def push():
    lst = x.split()
    que.append(lst[1])
def pop():
    if len(que) > 0:
        print(que.popleft())
    else:
        print('-1')

def empty():
    if len(que) == 0:
        print('1')
    else:
        print('0')

def size():
    print(len(que))

def front():
    if len(que) > 0:
        print(que[0])
    else:
        print('-1')

def back():
    if len(que) > 0:
        print(que[-1])
    else:
        print('-1')

N = int(sys.stdin.readline())

for _ in range(N):
    x = sys.stdin.readline().rstrip()
    if 'push' in x:
        push()
    elif x == 'pop':
        pop()
    elif x == 'size':
        size()
    elif x == 'empty':
        empty()
    elif x == 'front':
        front()
    elif x == 'back':
        back()
