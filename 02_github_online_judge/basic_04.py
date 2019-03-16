# Function
print('===== Function =====')

def say_hi(w):
    print('Hello,', w)

say_hi('Dragon')
say_hi('Jackson')

print('----------')

# Be careful about namespace
say_hi = 1 # say_hi function is replaced
# int = 12 << invalid, can't replace keyword
# print = 'hello' << invalid

# Later, we'll talk about local variables
#     and functional programming

# CamelCase and snake_case
print('===== CamelCase and snake_case =====')

# CamelCase     >>  AnAppleOfJack
# snake_case    >>  an_apple_of_jack

# CamelCase only be used in Class in Python
class BasketBall: # a basic class
    def __init__(self, balls):
        self.balls = balls

# Others use snake_case
def good_bye(s):
    print('Good bye,', s)
one_of_us = 'Jack'

print('----------')

# Special one: using all uppercase and _ to represent constant
DEFAULT_WIDTH = 13
MIN_HEIGHT = 1000

# Slice
print('===== Slice =====')

a = [5, 6, 7, 8, 9, 10]

a[3] # 8
a[1:3] # [6, 7] # represent elements that i >= 1 and i < 3
a[:2] # [5, 6]
a[3:] #[8, 9, 10]
a[:-2] # [5, 6, 7, 8]

print('----------')

a[-1] # 10
a[0:5:2] # [5, 7, 9]
a[3:0:-1] # [8, 7, 6]
a[:5:3] # [5, 8]
a[::-1]
