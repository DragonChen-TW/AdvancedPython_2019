# Local and Global
print('===== Local and Global =====')

candy_eaten = 3
# normal
def print_candy():
    print('I ate {} candies.'.format(candy_eaten))
    # candy_eaten = 0 # invalid
print_candy()

# modify global variable
def eat_candy():
    global candy_eaten # <<
    candy_eaten += 1
    print_candy()
eat_candy()

print('----------')

def foo():
    times = 0.5

    def bar():
        times = 3
        print(times)
    bar()

    print(times)
    print([n ** times for n in range(5)])
foo()

# there is global
times = 2
def foo():
    # there is nonlocal
    times = 0.5

    def bar():
        nonlocal times
        times = 3
        print(times)
    bar()

    print(times)
    print([n ** times for n in range(5)])
foo()

# Special Data Structure
print('===== Tuple =====')
n = (1, 3, 5)
print(n)
print(n[0], n[1])
# Tuple is immutable
# n[0] = 1 # Invalid

print('----------')

# uppack
a, b, c = n
print(a, b, c)

l = [(1, 3), (5, 7), (9, 11)]
for n1, n2 in l:
    print(n1, n2)

print('===== Set =====')

l = [2, 2, 6, 8]
s = set()


for n in l:
    s.add(n)
print(s)

print('----------')

# set could init with a "iterable" object
# also support Comprehension
s1 = set(i for i in range(1, 10))
print('s1', s1)
s2 = set(i for i in range(2, 20, 2))
print('s2', s2)

s3 = set('hello')
print('s3', s3)

print('----------')

print('interaction', s1.intersection(s2))
# print('interaction', s1 & s2) # the same
print('union', s1.union(s2))
# print('union', s1 | s2) # the same
