import sys

nums = sys.stdin.readline().split(' ')
a1 = int(nums[0])
an = int(nums[1])
d = int(nums[2])

if d > 0:
    end = an + 1
else:
    end = an - 1


print(' '.join([str(a) for a in range(a1, end, d)]))
