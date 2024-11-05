n2 = float(input())
n1 = float(input())


def triangle_area(a, b):
    area = a * b / 2
    print(f'{area:.12g}')


triangle_area(n1, n2)