obj = {}
while True:
    token = input()
    if token == 'end':
        [print(k, '===', v) for k, v in obj.items()]
        break

    name, val = token.split(' -> ')
    if val.isalpha():
        if val in obj.keys():
            obj[name] = obj[val]
        else:
            continue
    else:
        if name not in obj.keys():
            obj[name] = val
        else:
            obj[name] += f', {val}'

'''
Donald -> 2, 2, 2
Isacc -> 1
George -> John
John -> Isacc
end
'''
