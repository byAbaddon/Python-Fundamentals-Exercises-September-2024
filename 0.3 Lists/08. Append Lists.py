lst = [x for x in input().split('|')]
rv_lst = [x.strip().split() for x in reversed(lst) if x]
num_lst = [x for x in rv_lst if x]

for x in num_lst:
    print(*x, end=' ')

'''
1 2 3 |4 5 6 |  7  8
1 | | |||2   3 |4   5 6 | 7 8| -3 2   1||1 2|3|4|99 77
'''
