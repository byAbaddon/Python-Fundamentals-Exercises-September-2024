lst = sorted([int(x) for x in input().split()])
uniq = None
for x in lst:
    if uniq != x:
        print(x, '=>', lst.count(x))
    uniq = x

'''
8 2 2 8 2 2 3 7
'''
