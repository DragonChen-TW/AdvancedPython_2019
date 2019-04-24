import sys

n, m = sys.stdin.readline().split(' ')
n = int(n)
m = int(m)

print(6 * (n * m) \
    - 2 * (m - 1) * n \
    - 1 * (n - 1) * m)
