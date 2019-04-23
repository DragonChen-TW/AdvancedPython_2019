import sys

f = sys.stdin.readlines()

heights = f[0][:-1].strip().split(' ')
heights = [int(h) for h in heights]

# Progress Result
