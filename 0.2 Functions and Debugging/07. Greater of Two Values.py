v, a, b = [input() for _ in range(3)]

if v == 'int':
    print(max(int(a), int(b)))
elif v == 'char':
    print(a if ord(a) > ord(b) else b)
else:
    print(sorted([a,b], reverse=True)[0])

'''
2
16
'''