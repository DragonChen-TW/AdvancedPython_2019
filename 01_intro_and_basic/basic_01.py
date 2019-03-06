# Basic Operation
print('===== Basic Operation =====')

a = 7
b = 12

print(a + b)
print(a * b)
print(b / a)
print(a // 2)

print('----------')

a -= 2
b += 5

print(a % 2)
print(a ** 2)
print(b ** 0.5)

# Some Variables
print('===== Some Variables =====')

pig = ['big', 'middle', 'small']
print(pig)
print(pig[2])

animals = [pig,'dog','cat','lion', 13]
print(animals)
print(animals[0][1])

print('---------')

a_dict = {'a':'apple', 5:'cow', 'n':12, 7:13}
print(a_dict)
print(a_dict['a'])
print(a_dict[5])

print('---------')

a_dict = {
    'a':'apple',
    'b':'bang',
    'pi':3.1415,
}
print(a_dict)
a_dict['b'] = 'bed'     # modify
a_dict['d'] = 'done'    # or insert one
print(a_dict)
