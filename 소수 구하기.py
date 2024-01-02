#에라토스테네스의 체 이용
import sys
def prime(M, N):
    lst = [True]*(N+1)
    for i in range(2, int(N**0.5)+1):
        if lst[i-M] == True:
            for j in range(2*i, N+1, i):#시작, 끝 간격
                lst[j-M] = False
    result = [i for i in range(max(2, M), N+1) if lst[i-M] == True]
    for v in result:
        print(v)
M, N = map(int, sys.stdin.readline().split())
prime(M, N)