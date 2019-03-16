import sys

for s in sys.stdin:
    s = s[:-1] # delete the last char '\n'
    s_reverse = s[::-1] # reverse

    if s == s_reverse:
        print('yes')
    else:
        print('no')
