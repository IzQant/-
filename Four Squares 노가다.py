input = __import__('sys').stdin.readline
n = int(input())
L = [i**2 for i in range(1,int(n**0.5)+1)]
if n in L:
    print(1)
    exit()
for a in range(1,int(n**0.5)+1):
    if n - a**2 in L:
        print(2)
        exit()
for a in range(1,int(n**0.5)+1):
    for b in range(1,int(n**0.5)+1):
        if n - a**2 - b**2 in L:
            print(3)
            exit()
print(4)