input = __import__('sys').stdin.readline

def gcd(A, B):
    while B > 0:
        A, B = B, A%B   
    return A
def lcm(A, B):
    return A*B // gcd(A, B)

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))