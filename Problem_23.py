from Problem_21 import d

max = 28124
nums = []
abundant_nums = []
for n in range(1, max):
    nums.append(True)
    if d(n) > n:
        abundant_nums.append(n)
print(nums)
print(abundant_nums)
for a in abundant_nums:
    for b in abundant_nums:
        if a + b < len(nums):
            nums[a + b] = False
            # print(a + b, a, b)
        else:
            break

s = 0

for i in range(len(nums)):
    if nums[i]:
        # print(s, i)
        s += i

print(s)
# 4179871 - correct
