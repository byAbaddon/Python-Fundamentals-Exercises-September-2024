import re

while True:
    code = input()
    if code == 'Over!': break
    m = int(input())
    pattern = r'^([0-9]+)([a-zA-Z]+)([^a-zA-Z]*)$'
    match = re.match(pattern, code)
    try:
        first_digits = [int(x) for x in match.group(1) if x.isdigit()]
        message = match.group(2)
        second_digits = [int(x) for x in match.group(3)if x.isdigit()]
        all_digits = first_digits + second_digits
        collect = ''
        if len(message) == m:
            for i in all_digits:
                if len(message) > i:
                    collect += message[i]
                else:
                    collect += ' '
            print(f'{message} == {collect}')
    except:
        continue






'''
1234test4321
4
0000oooo0000
4
Over!
'''


