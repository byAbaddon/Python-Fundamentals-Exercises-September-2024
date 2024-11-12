token = [input() for x in range(int(input()))]
rows = [''.join(c for c in row if c.isalpha()) for row in token]

big_row = 0
char = ''
pir = 1

for r in reversed(rows):
    for c in set(r):
        if r.count(c) > big_row:
            big_row = r.count(c)
            char = c

for row in rows:
    if char in row:
        count = row.count(char)
        if count >= pir:
            print(char * pir)
            pir += 2



'''
9
abc
bsc
abb
aaa
aaaaab
bbbaaaaaaa
aaaaaaaaa
bbbbb
bbbbbbb
'''