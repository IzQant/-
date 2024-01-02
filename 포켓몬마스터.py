input = __import__('sys').stdin.readline

N, M = map(int, input().split())
#딕셔너리 사용?
po = list(input().strip() for _ in range(N))
question = list(input().strip() for _ in range(M))
dic = {}
for i in range(len(po)):
    dic[po[i]] = str(i+1)
cid = {v:k for k, v in dic.items()}#value값으로 key를 찾을 때는 딕셔너리 뒤집고 찾기
for i in question:
    if i in dic.keys():
        print(dic[i])
    else:
        print(cid.get(i))