import sys
K = int(sys.stdin.readline())
lst = []
for i in range(K):
    a = int(sys.stdin.readline().strip())
    if a == 0:
        lst.pop()
    else:
        lst.append(a)
print(sum(lst))