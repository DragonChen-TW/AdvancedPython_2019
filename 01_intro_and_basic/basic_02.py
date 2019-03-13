# Basic Function
print('===== Basic Function =====')

a = [1, 3, 5]
b = 7
print(type(a), type(b))
print(type(str(b)))

print('----------')

a_dict = {
    'a':'apple',
    'b':'bang',
    'pi':3.1415,
}
print('length: ', len(a_dict))
print('length: ', len('Hello, Python!'))

print('----------')

a = [2, 4, 6, 8]
a.append(10)
print(a)
print(a.index(8))

# String and List
print('===== String =====')

a = 'Jackson'
b = 3
print(a, 'have', b, 'apples.')
print('{} have {} apples'.format(a, b)) # 後面這種會用最多
print(f'{a} have {b} apples') # Python 3.6 開始支援 新用法

print('----------')

s = 'small'
print(s)
s = "Hello\nSmall Dragon"
print(s) # print 會輸出 \n 跳脫字元
s = '''
Two roads diverged in a yellow wood,
And sorry that I could not travel both
And be one traveler, long I stood
'''  # 多行字串適合使用 '''
print(s)

# Function
def hello(s):
    '''
    This function is for say hello
    '''
    print('hello', s)

hello('Annie')
hello('')
