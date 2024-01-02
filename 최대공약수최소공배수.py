a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a%b    #a와 b가 b와 a를 b로 나눈 나머지와 같음-유클리드 호제법
    return a
def lcm(a, b):
    return a*b // gcd(a, b)
print(gcd(a, b))
print(lcm(a, b))


