# Class(optimizebject) inititalize
class Node: # Naming Class start with uppercase
    pass
n = Node()
print(n)

class Node:
    color = 'red'
    # always naming self represent yourself(this class)
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = Node(1, 3)
# You will never have to call the `object.__inin__(args)`
# It gets call automatically when you create class
print(n.x, n.y, n.color)

n2 = Node(2, 5)
print(n2.x, n2.y, n2.color)

print('----------')

print(n)
print(type(n))

print('----------')

# Move on
class Circle:
    def __init__(self, x, y, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def calculate_area(self, degree=None):
        area = (self.radius ** 2) * 3.14
        if degree:
            area = area * degree / 360
        self.area = area

c = Circle(3, 5)
c = Circle(4, 4, 3)
c.calculate_area()
print(c.area)
