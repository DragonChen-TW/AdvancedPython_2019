import sys
lines = [l for l in sys.stdin]
# lines = [2, 1, 5, 5, 35]

# Another Soultion
# Directly generate numbers

n = int(lines[0]) # how many pairs of input
for i in range(1, n + 1):
    l = i * 2 - 1
    a = int(lines[l])
    b = int(lines[l + 1])

    # Your turn!
    start = int(a ** 0.5)
    if start ** 2 < a:
        start += 1
    end = int(b ** 0.5) + 1

    ans = sum([n ** 2 for n in range(start, end)])

    print('Case {}: {}'.format(i, ans)) # ans
    # ans should be 5, 50
