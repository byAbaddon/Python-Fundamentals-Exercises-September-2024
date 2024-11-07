num_list = input().split()
p = int(input())
print(*map(lambda x: int(x) * p, num_list))


'''
1 3 12 4
4
'''