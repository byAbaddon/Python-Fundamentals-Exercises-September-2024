import math

n_lst = map(int, input().split())
collect = []
for num in n_lst:
    if num > 0:
        if int(math.sqrt(num)) ** 2 == num:
            collect.append(num)

print(*sorted(collect, reverse=True))



'''
3 16 4 5 6 8 9

'''