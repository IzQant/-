def solution(scores):
    answer = 0
    temp = [l for l in scores]

    for k in range(len(scores)):
        if scores[k] == 'X':
            temp = [l for l in scores]
            temp[k] = 'O'
        cnt = 0
        ans = 0
        for i in temp:
            if i == 'O':
                cnt += 1
                ans += cnt
            else:
                cnt = 0
            
        if answer < ans:
            answer = ans
    return cnt