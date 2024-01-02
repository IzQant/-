#누적합 이용!
import sys
while True:
    A = sys.stdin.readline().rstrip()

    if A == '.':
        quit()
    result = []
    balanced = False

    for i in A:
        if i == "(" or i == "[":
            result.append(i)
        elif i == ")":
            if result and result[-1] == "(":
                result.pop()
            else:
                balanced = True
                break
        elif i == "]":
            if result and result[-1] == "[":
                result.pop()
            else:
                balanced = True
                break

    if not result and balanced == False:
        print('yes')
    else:
        print('no')