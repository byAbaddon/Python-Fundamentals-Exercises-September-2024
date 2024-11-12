txt = input()
while True:
    try:
        command, v1, *v2 = input().split()
        v1 = int(v1)
        if command == 'Left':
            while v1:
                char = txt[0]
                txt = txt[1:] + char
                v1 -= 1
        if command == 'Right':
            while v1:
                char = txt[-1]
                txt = char + txt[:-1]
                v1 -= 1
        if command == 'Insert':
            if len(txt) <= v1:
                txt += v2[0]
            else:
                c_txt = ''
                for i, c in enumerate(txt):
                    if i == v1:
                        c_txt += v2[0]
                    c_txt += c
                txt = c_txt
        if command == 'Delete':
            txt = txt[:v1] + txt[int(v2[0]) + 1:]
    except:
        print(txt)
        exit()



'''
The Lone Ranger
Delete 0 7
Insert 0 Power
Insert 12 s
end
'''