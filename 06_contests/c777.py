import sys

n, m = sys.stdin.readline().split(' ')
n = int(n)
m = int(m)

n1, n2, n3 = 0, 1, 2
i = 2

if n == 1:
    start = 1
else:
    while n3 < n:
        n1, n2, n3 = n2, n3, n1+n2+n3
        i += 1
    start = i

while n3 <= m:
    n1, n2, n3 = n2, n3, n1+n2+n3
    i += 1
print(i - start)
