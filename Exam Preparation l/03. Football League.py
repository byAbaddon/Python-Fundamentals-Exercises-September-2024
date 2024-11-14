import re

lst = [x for x in iter(input, 'final')]
key = lst.pop(0)

pattern = r'{0}(.*?){0}.*?{0}(.*?){0}.*?(\d+:\d+)'.format(re.escape(key))
obj = {}
f_point = None
s_point = None
f_goals = 0
s_goals = 0

for tim in lst:
    match = re.findall(pattern, tim)[0]
    f = match[0].upper()[::-1]
    s = match[1].upper()[::-1]
    r = match[2]

    f_r, s_r = map(int, match[2].split(':'))
    f_goals = int(f_r)
    s_goals = int(s_r)

    if f_r > s_r:
        f_point = 3
        s_point = 0
    elif f_r < s_r:
        f_point = 0
        s_point = 3
    else:
        f_point = 1
        s_point = 1

    obj.setdefault(f, {'points': 0, 'goals': 0})
    obj[f]['points'] += f_point
    obj[f]['goals'] += f_goals

    obj.setdefault(s, {'points': 0, 'goals': 0})
    obj[s]['points'] += s_point
    obj[s]['goals'] += s_goals


sort_obj = dict(sorted(obj.items(), key=lambda x: (-x[1]["points"], x[0])))


print('League standings:')
index = 0
for k, v in sort_obj.items():
    index += 1
    print(f'{index}. {k} {v["points"]}')


sort_obj_by_goals = dict(sorted(sort_obj.items(), key=lambda x: -x[1]["goals"]))

print('Top 3 scored goals:')
index = 0
for k, v in sort_obj_by_goals.items():
    print(f'- {k} -> {v["goals"]}')
    index += 1
    if index == 3: break



'''
??
??ecnarF?? ??kramneD?? 0:0
..??airagluB??32 ??dnalgnE??gf 3:2
Fg??NIAPS?? fgdrt%#$??YNAMREG??gtr 3:4
??eCnArF?? >>??yLATi??<< 2:2
final
'''
