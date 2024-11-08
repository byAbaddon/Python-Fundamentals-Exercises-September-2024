lst = []
for v1, v2 in [x.split(' : ') for x in iter(input, 'Over')]:
    try:
        lst.append((v2, int(v1)))
    except:
        lst.append((v1, str(v2)))

for name, phone in sorted(lst, key=lambda x: x[0]):
    print(name, '->', str(phone))



'''
14284124 : Alex
Gosho : 088423123
Ivan : 412048192
123123123 : Nanyo
Pesho : 150925812
Over
'''