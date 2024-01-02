input = __import__('sys').stdin.readline

n, m = map(int, input().split())
lst = [0]*(n+1)
lst[1] = 1
for i in range(2, n+1):
    lst[i] = lst[i-1]*i
print(lst[n]//(lst[m]*lst[n-m]))