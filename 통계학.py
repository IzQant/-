import sys
N = int(sys.stdin.readline())
nums = [0]*N
j = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[j] = num
    j += 1
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
if len(nums) > 1:
    for i in nums:
        dict = dict.fromkeys(nums, nums.count(i))
    new = list([k for k, v in dict.items() if max(dict.values()) == v])
    print(new[1])
else:
    print(nums[0])

print(max(nums) - min(nums))