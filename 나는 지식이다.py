input = __import__('sys').stdin.readline

N = int(input())
lst = []
fun = 0

lst1 = []
lst2 = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

for i in lst:
    if i[0] <= i[1]:
        lst1.append(i)
    if i[0] > i[1]:
        lst2.append(i)
lst1.sort(key = lambda x: (x[0], x[1]))
lst2.sort(key = lambda x: (x[1], x[1]))
#print(lst1)
#print(lst2)


for j in lst1:
    if fun - j[0] >= 0: 
        fun = fun - j[0] + j[1]
    else:
        print(0)
        quit(0)
lst2.reverse()
for v in lst2:
    if fun - v[0] >= 0:
        fun = fun - v[0] + v[1]
    else:
        print(0)
        quit(0)

if fun >= 0:
    print(1)
else:
    print(0)