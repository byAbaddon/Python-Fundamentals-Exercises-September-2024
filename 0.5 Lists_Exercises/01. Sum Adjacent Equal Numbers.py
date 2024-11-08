lst = [float(x) for x in input().split()]

while True:
    merged = False
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            lst[i] = lst[i] + lst[i + 1]
            del lst[i + 1]
            merged = True
            break
    if not merged:
        break

print(*lst)

'''
3 3 6 1
'''
