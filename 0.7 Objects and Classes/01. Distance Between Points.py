import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(p1, p2):
    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    distance = math.sqrt(a ** 2 + b ** 2)
    return distance


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print(f'{calc_distance(p1, p2):.3f}')



'''
3 4
6 8
'''