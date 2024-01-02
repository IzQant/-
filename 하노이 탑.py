input = __import__('sys').stdin.readline

def hanoi(n, F, T, a):
    if n <= 20:
        if n == 1:
            print(F, a)
            return
        hanoi(n-1, F, a, T)
        print(F, a)
        hanoi(n-1, T, F, a)

n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)