obj = {}

for i, c in enumerate(input()):
    obj.setdefault(c, []).append(str(i))

for k, v in obj.items():
    print(f"{k}:{'/'.join(v)}")


'''
abababa
'''
# --------------------------------------(2)--------------------


c_i = [(c, i) for i, c in enumerate(input())]

obj = {}
for c, i in c_i:
    if c not in obj:
        obj[c] = ''
    obj[c] += str(i) + '/'

for k, v in obj.items():
    print(f"{k}:{v.rstrip('/')}")

'''
abababa
'''
