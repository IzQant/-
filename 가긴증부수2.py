input = __import__('sys').stdin.readline

N = int(input())
A = list(map(int, input().split()))
lis = [0]

for i in A:
    if lis[-1] < i:
        lis.append(i)
    else:
        left = 0
        right = len(lis)

        while left < right:
            mid = (left + right)//2
            if lis[mid] < i:
                left =  mid + 1
            else:
                right = mid
        lis[right] = i
print(len(lis)-1)