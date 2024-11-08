obj = {}
for x in iter(input, 'exam time'):
    com, item, *val = x.split()
    if com == 'stock':
        obj[item] = obj.get(item, 0) + int(*val)
    if com == 'buy':
        if item not in obj.keys():
            print(item, "doesn't exist")
        elif obj[item] <= 0:
            print(item, "out of stock")
        else:
            obj[item] -= int(*val)

v = {print(*(k, "->", v)) for k, v in obj.items() if v > 0}

'''
stock Boca_Cola 10
stock Boca_Cola 10
stock Kay's 3
stock Kay's 2
shopping time
buy Boca_Cola 5
buy Kay's 5
exam time
'''
