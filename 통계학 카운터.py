import sys
from collections import Counter
N = int(sys.stdin.readline())
nums = [0]*N
j = 0
for _ in range(N):
    n = int(sys.stdin.readline())
    nums[j] = n
    j += 1
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
counter = Counter(nums).most_common()
maximum = counter[0][1]
if len(counter) > 1:
    M = []
    for v in counter:
        if v[1] == maximum:
            M.append(v[0])
    if len(M) == 1:
        print(M[0])
    else:
        print(M[1])
else:
    print(counter[0][0])

print(max(nums) - min(nums))