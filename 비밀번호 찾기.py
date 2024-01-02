input = __import__('sys').stdin.readline
N, M = map(int, input().split())
#얘도 딕셔너리 사용
pw = list((input().split()) for _ in range(N))
question = list(input().strip() for _ in range(M))
dic = {}
for i in range(N):
    dic[pw[i][0]] = pw[i][1]
for i in question:
    print(dic[i], sep='')