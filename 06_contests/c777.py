import sys

fabos = [1, 1]
def f(n):
    if n < len(fabos) and fabos[n]:
        return fabos[n]

    if n == 0 or n == 1:
        return 1
    else:
        temp = fabos[n] = f(n - 1) + f(n - 2)
        return temp


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
