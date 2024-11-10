class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top - self.height

    def is_inside(self, other):
        return (self.left >= other.left and
                self.right <= other.right and
                self.top <= other.top and
                self.bottom >= other.bottom)


def read_rectangle():
    left, top, width, height = map(int, input().split())
    return Rectangle(left, top, width, height)

rect1 = read_rectangle()
rect2 = read_rectangle()

if rect1.is_inside(rect2):
    print("Inside")
else:
    print("Not inside")



'''
4 -3 6 4
2 -3 10 6
'''