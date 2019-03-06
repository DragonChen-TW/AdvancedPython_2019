# If-Else
print('===== If-Else =====')

a = 3
l = [1, 2, 3]
if a in l:
    print('a in l')
else:
    print('a not in l')

print('----------')

a = 10

if a == 5:
    print('a == 5')
elif a < 10:
    print('a < 10')
else:
    print('a >= 10')

# For Loop
print('===== For Loop =====')

nums = [5, 1, 7, 9]
for n in nums:
    print(n)

print('----------')

for i in range(1, 10, 2):
    print(i)

# Python 裡不要像下面這樣寫
l = []
for i in range(1, 10, 2):
    l.append(i * 10)
print(l)

# 可以這樣，跑很快，但是你可能看不懂
l = list(map(lambda x:x * 10, range(1, 10, 2)))
print(l)

# 這樣最簡單，也超級快
l = [i * 10 for i in range(1, 10, 2)]
print(l)
