st = input()
char_set = sorted(set(x for x in st), key=st.index)
[print(f'{x} -> {st.count(x)}') for x in char_set]


'''
aaabbaaabbbccc
'''