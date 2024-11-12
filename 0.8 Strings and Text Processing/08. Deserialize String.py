positions = [x.split(':') for x in iter(input, 'end')]
index = max(int(i) for _, pos in positions for i in pos.split('/'))
s = [''] * (index + 1)

for c, pos in positions:
    for i in pos.split('/'):
        s[int(i)] = c

print(''.join(s))



'''
a:0/2/4/6
b:1/3/5
end
'''

