lst = [int(x) for x in input().split() if int(x) > 0]
if not len(lst):
    print('empty')
else:
    # print(*lst[::-1])
    print(*reversed(lst))

'''
10 -5 7 9 -33 50
'''