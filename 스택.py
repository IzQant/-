import sys
L = []
def push():
    lst = x.split()
    L.append(lst[1])
def pop():
    if len(L) > 0:
        print(L.pop())
    else:
        print('-1')

def empty():
    if len(L) == 0:
        print('1')
    else:
        print('0')

def size():
    print(len(L))

def top():
    if len(L) > 0:
        print(L[-1])
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
    elif x == 'top':
        top()