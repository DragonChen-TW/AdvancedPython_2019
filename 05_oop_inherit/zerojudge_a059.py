import sys
lines = [l for l in sys.stdin]
# lines = [2, 1, 5, 5, 35]

def is_full(n):
    n = n ** 0.5
    if n == int(n):
        return True
    else:
        return False

n = int(lines[0]) # how many pairs of input
for i in range(1, n + 1):
    l = i * 2 - 1
    a = int(lines[l])
    b = int(lines[l + 1])

    # Your turn!
    temp = [n for n in range(a, b + 1) if is_full(n)]
    ans = sum(temp)

    print('Case {}: {}'.format(i, ans)) # ans
	# ans should be 5, 50
