#누적합 이용! but 시간초과
import sys
while True:
    A = sys.stdin.readline().rstrip()

    balanced = True
    result = []
    if A == '.':
        break

    for i in A:
        if i == "(" or i == "[":
            result.append(i)
        elif i == ")":
            if not result:
                balanced = False
                break
            top = result.pop()
        elif i == "]":
            if not result:
                balanced = False
                break
            top = result.pop()
        if (top == "(" and i == ")") or (top == "[" and i == "]"):
            continue
        else:
            balanced = False
            break
    if result:
        balanced = False

if balanced:
    print('yes')
else:
    print('no')