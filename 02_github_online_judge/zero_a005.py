import sys

for s in sys.stdin:
    nums = s.split(' ')
    a, b = nums # unpack trick
    # or easy way
    # a = nums[0]
    # b = nums[1]

    a, b = int(a), int(b) # unpack trick
    # or easy way
    # a = int(a)
    # b = int(b)
    print(a + b)
