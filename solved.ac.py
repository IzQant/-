input = __import__('sys').stdin.readline

def halfup(n:float)->int:
    if n < 0:
        return -halfup(-n)
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    
def solved(n):
    idealist = []
    for _ in range(n):
        a = int(input())
        idealist.append(a)
    idealist.sort()
    n = n*15/100
    rm = halfup(n)
    if rm == 0:
        idealist = idealist
    else:
        idealist = idealist[rm:-rm]
    if len(idealist) == 0:
        result = 0
    else:
        result = sum(idealist) / len(idealist)
    return halfup(result)

n = int(input())
if n == 0:
    result = 0
    print(result)
else:
    print(solved(n))