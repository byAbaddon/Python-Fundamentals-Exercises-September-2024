n = int(input())


def top_down_rows(n):
    print('-' * n * 2)


def body(n):
    for _ in range(n -2):
        print('-' + '\\/' * (n - 1) + '-')


def call(n):
    top_down_rows(n)
    body(n)
    top_down_rows(n)


call(n)


'''
4
'''