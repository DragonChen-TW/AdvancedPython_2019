class Shape:
    def __init__(self):
        self.data = ['_' for _ in range(10)]
    def print_out(self):
        print(''.join(self.data))

class Even(Shape):
    def draw_func(self, x):
        if x % 2 == 0:
            return True
        else:
            return False

class ThirdBiggerFive(Shape):
    def draw_func(self, x):
        if x % 3 == 0 or x > 5:
            return True
        else:
            return False

def draw(Obj):
    o = Obj()
    for x in range(0, 10):
        if o.draw_func(x):
            o.data[x] = 'X'
    return o

even = draw(Even)
even.print_out()
third = draw(ThirdBiggerFive)
third.print_out()
