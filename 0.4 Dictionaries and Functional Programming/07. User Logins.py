obj = {}
is_login = False
count = 0

for x in iter(input, 'end'):
    token, *val = x.split(' -> ')
    if token == 'login':
        is_login = True
        continue

    if not is_login:
        obj[token] = val[0]
    else:
        if token in obj and obj[token] == val[0]:
            print(f"{token}: logged in successfully")
        else:
            print(f"{token}: login failed")
            count += 1

print('unsuccessful login attempts:', count)

'''
ivan_ivanov -> java123
pesh0 -> qwerty
stamat4e -> 111111
princess_penka -> MyPrince
login
pesh0 -> qwertt
ivan_ivanov -> java123
stamat4e -> 111112
princess_penka -> MyPrince
end
'''