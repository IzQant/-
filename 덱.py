import sys
from collections import deque
que = deque()
def push_front():
    lst = x.split()
    que.appendleft(lst[1])
def push_back():
    lst = x.split()
    que.append(lst[1])
def pop_front():
    if len(que) > 0:
        print(que.popleft())
    else:
        print('-1')
def pop_back():
    if len(que) > 0:
        print(que.pop())
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
    if 'push_front' in x:
        push_front()
    elif 'push_back' in x:
        push_back()
    elif x == 'pop_front':
        pop_front()
    elif x == 'pop_back':
        pop_back()
    elif x == 'size':
        size()
    elif x == 'empty':
        empty()
    elif x == 'front':
        front()
    elif x == 'back':
        back()
