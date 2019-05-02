import sys

f = sys.stdin.readlines()

heights = f[0][:-1].strip().split(' ')
# print(heights)
heights = [int(h) for h in heights]


na = int(f[1])

# normal way
ans = 0
for h in heights:
    if na + 30 >= h:
        ans += 1
print(ans)

# Python compressed way
# print(sum([1 for h in heights if na + 30 >= h]))
