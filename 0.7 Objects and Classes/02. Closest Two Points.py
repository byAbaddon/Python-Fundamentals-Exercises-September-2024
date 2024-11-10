import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def find_closest_points(points):
    min_distance = float('inf')
    closest_pair = None


    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calc_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair


n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))


min_distance, (p1, p2) = find_closest_points(points)
print(f"{min_distance:.3f}")
print(f"({p1.x}, {p1.y})")
print(f"({p2.x}, {p2.y})")



'''
3
12 -30
6 18
6 18
'''