class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def calculate_distance(point1, point2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.width = int(Point.calculate_distance(upper_left, upper_right))
        self.height = int(Point.calculate_distance(upper_left, bottom_left))

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


boxes = []
while True:
    line = input()
    if line == "end":
        break
    coords = line.split(" | ")
    box = Box(
        Point(*map(int, coords[0].split(":"))),
        Point(*map(int, coords[1].split(":"))),
        Point(*map(int, coords[2].split(":"))),
        Point(*map(int, coords[3].split(":")))
    )
    boxes.append(box)

for box in boxes:
    print(f"Box: {box.width}, {box.height}")
    print(f"Perimeter: {box.calculate_perimeter()}")
    print(f"Area: {box.calculate_area()}")



'''
0:2 | 2:2 | 0:0 | 2:0
-3:0 | 0:0 | -3:-3 | 0:-3
-2:2 | 2:2 | -2:-2 | 2:-2
end
'''