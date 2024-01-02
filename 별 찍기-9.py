N = int(input())
for i in range(1, N+1):
    print(" "*(i-1)+"*"*(2*N-2*i+1)+" "*(i-1))
    print()
for j in range(1, N):
    print(" "*(N-j-1)+"*"*(2*j+1)+" "*(N-j-1))
    print()
