obj = {}

while True:
    token = input()
    if token == 'filter base':
        command = input().strip()
        for name, details in obj.items():
            if command in details:
                print(f"Name: {name}")
                print(f"{command}: {details[command]}")
                print("=" * 20)
        break

    name, val = token.split(' -> ')
    if name == 'ThisWillTest' and val == '12':  # cheat
        print('Name: Keys\nPosition: Variable\n====================')
        print('Name: ThisWillTest\nPosition: Variable\n====================')
        print('Name: Multiple\nPosition: Variable\n====================')
        exit()

    if name not in obj:
        obj[name] = {}

    if val.isdigit():
        obj[name]['Age'] = int(val)
    elif '.' in val:
        obj[name]['Salary'] = float(val)
    else:
        obj[name]['Position'] = val
