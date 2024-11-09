s_key, s_val, loop = input(), input(), int(input())

while loop:
    loop -= 1
    key, val = input().split(' => ')
    if s_key in key:
        print(key + ':')
        for v in val.split(';'):
            if s_val in v:
                print('-' + str(v))

'''
bug
X
3
invalidkey => testval;x;y
debug => XUL;ccx;XC
buggy => testX;testY;XtestZ
'''
