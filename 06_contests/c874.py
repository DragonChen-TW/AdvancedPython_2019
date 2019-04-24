import sys

n = sys.stdin.readline()
n = int(n)

# # solution 1
# ans = 0
# for i in range(0, n):
#     ans += (4 ** i)
#
# print(ans)

# solution 2
print((4 ** n - 1) // 3)
