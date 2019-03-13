# If-Else
print('===== If-Else =====')

a = 3
l = [1, 2, 3]

print('hello')

if a < 5:
    print('a < 5')

if b in l:
    print('a in l')
else:
    print('a not in l')

print('----------')

a = 10

if a == 5:
    print('a == 5')
elif a < 10:
    if a == 7:
        pass
    else:
        pass
else:
    print('a >= 10')

# For Loop
print('===== For Loop =====')

nums = [5, 1, 7, 9]
for n in nums:
    print(n)

print('----------')

for i in range(5):
    print(i)
print()
for i in range(5, 11):
    print(i)
print()
for i in range(1, 10, 2):
    print(i)

# 和 C 語言的 for 比較
# for(i = 1;i < 10;i += 2){
#
# }

# List Comprehension
print('===== List Comprehension =====')

# 其他語言的寫法
# Python 裡盡最大可能不要用這寫法
l = []
for i in range(1, 10, 2):
    l.append(i * 10)
print(l)

# 可以這樣，跑很快，但是你可能看不懂
l = list(map(lambda x:x * 10, range(1, 10, 2)))
print(l)

# 這樣最簡單，也超級快
l = [i for i in range(1, 10, 2)]
print(l)

# 額外小技巧
print(list(range(1, 10, 2)))
