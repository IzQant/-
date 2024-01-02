import sys
T = int(sys.stdin.readline())
test = [int(sys.stdin.readline()) for _ in range(T)]


def fibo(x):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if len(zero) <= x:
        for i in range(len(zero), x + 1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
    return zero[x], one[x]


for i in test:
    a, b = fibo(i)
    print(a, b)
    