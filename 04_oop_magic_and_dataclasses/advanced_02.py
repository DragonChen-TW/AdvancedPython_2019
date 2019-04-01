# Iter way
print('===== Iter way =====')

nums = ['a', 'c', 'e']

# If you are a C/JAVA user
# not recomended in Python
for i in range(0, len(nums)):
    n = nums[i]
    # print(i, n) # our purpose

# If you learn Python for two weeks
# the i is not good at all
i = 0
for n in nums:
    # print(i, n) # our purpose
    i += 1

print('----------')

# remember the unpack I mentioned last week?
temp = (1, 'apple')
i, n = temp # < unpack
print('unpack i={} n={}'.format(i, n))

# the most Pythonic iter way
# put "iterable" object inside enumerate
for i, n in enumerate(nums):
    print(i, n)
    # ...


# # Magic Method
print('===== Magic Method =====')
# Magic Method is some special function you can use in Python
# Naming Rule: __something__
# For Example: __name__, __str__

modules = ['os','time']
mode = 1
if mode == 1:
    __import__(modules[1]) # dynamic import module
    
# you could notice how atom highlight the name
# cuz magic method is a kind of keyword


print(__name__)
# Python build a script into a module in runtime
# __name__ will show that module's name
# If you use the command `python some_scrip.py`, __name__ will be '__main__'

if __name__ == '__main__':
    pass
    # the way Python do main FUNCTION
    # like `int main()` in c language

# run `python advanced_03.py` and `python advanced_04.py`
# to see the difference
