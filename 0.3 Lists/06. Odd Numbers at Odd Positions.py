lst = input().split()

for i in range(len(lst)):
    if int(i & 1 and lst[i]) & 1:
        print('Index', i, '->', lst[i])

'''
2 3 5 2 7 9 -1 -7
'''
