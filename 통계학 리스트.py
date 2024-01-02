import sys
def average(N):
    if sum(lst)//N < 0 and sum(lst)//N > -1:
         print(0)
    else:
         print(sum(lst)//N)
def middle(N):
    lst.sort()
    if N == 1:
        print(lst[0])
    else:
        print(lst[N//2])

def count():
    lst.sort()
    if N == 1:
        print(lst[0])
    else:
        for i in lst:
            cnt.append(lst.count(i))
        for i in lst:
            if lst.count(i) == max(cnt):
                M.append(i)
        m = list(set(M))
        m.sort()
        if len(m) > 1:
            print(m[1])
        else:
            print(m[0])

def splash():
    if N == 1:
        print(0)
    else:
        lst.sort()
        if lst[0] < 0 and lst[-1] < 0:
            print(abs(lst[0]) - abs(lst[-1]))
        elif lst[0] < 0 and lst[-1] > 0:
            print(abs(lst[0]) + abs(lst[-1]))
        else:
            print(lst[-1] - lst[0])
             
             
N = int(sys.stdin.readline())
lst = []
cnt = []
M = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
average(N)
middle(N)
count()
splash()
