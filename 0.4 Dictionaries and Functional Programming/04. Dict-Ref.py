obj = {}
for name, val in [x.split(' = ') for x in iter(input, 'end')]:
    try:
        obj[name] = int(val)
    except:
        if val in obj:
            obj[name] = obj[val]

v = {print(*(k, "===", v)) for k, v in obj.items()}

'''
Vladi = 5
Ivo = Vladi
Vladi = Bok
Nakov = Bok
Bok = 7
Ivo = Bok
end
'''
