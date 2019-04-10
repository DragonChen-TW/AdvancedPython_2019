class Items: # normal way
    def __init__(self, items=''):
        self.items = items

    def add(self, s):
        self.items = self.items + ',' + s

    def print_out(self):
        return self.items

# Logic part is hard to read and reuse
item = Items('Mac')
item.add('Linux')
item.add('Windows')
print(item.print_out())


# Using Magic Method

class Items:
    def __init__(self, items=''):
        self.items = items

    def __add__(self, s): # magic!
        self.items = self.items + ',' + s
        return self

    def __repr__(self):
        return self.items

# Logic part is readable now
# And like normal Python now
item = Items('Mac')
item = item + 'Linux' + 'Windows'
# Items('Mac') + 'Linux' + 'Windows' # or just one line
print(item)

# 想想看兩種設計方法的給你的感覺
# 體會一下設計物件的思路、主函式的邏輯
# 多用這類設計方法和
# coding style 會讓你的 Programming 走得更高更遠

print('----------')

# Magic with Class
class String:
    def __init__(self, init_s=''):
        self.data = init_s

    def __len__(self):       # auto bind to len()
        return len(self.data)

    def __eq__(self, s2):    # auto bind to ==
        return len(self.data) == len(s2.data)

    def __repr__(self):      # auto bind to print()
        return "String {} Length: {}".format(
            self.data,
            len(self)
        )


if __name__ == '__main__':
    s1 = String('hello')
    s2 = String('worldworld')

    print(s1)
    print(s2)
    print(len(s1))
    print(s1.data == s2.data) # normal string comparison
    print(s1 == String('world')) # compare with length
