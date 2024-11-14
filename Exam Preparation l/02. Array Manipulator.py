lst = [int(x) for x in input().split()]

while True:
    token = input()
    if token == 'end':
        print(lst)
        break

    command, v1, *v2 = token.split()

    if command == 'exchange':
        v1 = int(v1)
        if v1 >= len(lst) or v1 < 0:
            print('Invalid index')
        else:
            lst = lst[v1 + 1:] + lst[:v1 + 1]

    elif command == 'max':
        indices = [i for i, x in enumerate(lst) if (not x & 1 if v1 == 'even' else x & 1)]
        if not indices:
            print('No matches')
        else:
            max_index = max(indices, key=lambda i: (lst[i], i))
            print(max_index)

    elif command == 'min':
        indices = [i for i, x in enumerate(lst) if (not x & 1 if v1 == 'even' else x & 1)]
        if not indices:
            print('No matches')
        else:
            min_index = min(indices, key=lambda i: (lst[i], -i))
            print(min_index)

    elif command == 'first':
        count = int(v1)
        if count > len(lst) or count <= 0:
            print('Invalid count')
        else:
            result = [x for x in lst if (not x & 1 if v2[0] == 'even' else x & 1)][:count]
            print(result)

    elif command == 'last':
        count = int(v1)
        if count > len(lst) or count <= 0:
            print('Invalid count')
        else:
            result = [x for x in lst if (not x & 1 if v2[0] == 'even' else x & 1)][-count:]
            print(result)


'''
1 3 5 7 9
exchange 1
max odd
min even
first 2 odd
last 2 even
exchange 3
end
'''