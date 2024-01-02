T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    print((N%H if N%H != 0 else H),'%02d'%(N//H+1 if N%H else N//H), sep="")