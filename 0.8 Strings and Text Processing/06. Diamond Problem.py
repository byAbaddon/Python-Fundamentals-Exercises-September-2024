import re

txt = input()
match = re.findall(r"<\w+>", txt)
match_digit = [re.findall(r"\d+", x) for x in match]
carats = [sum(map(int, ''.join(x))) for x in match_digit]

if not carats:
    print('Better luck next time')
else:
    [print(f'Found {x} carat diamond') for x in carats]


'''
empty<2big32diamond>useless<1another02Diamond>
'''
