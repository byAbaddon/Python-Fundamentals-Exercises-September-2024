import re

separators = r"[,\;\:\.\!\(\)\"\'\\/\[\]\s]+"
lc = []
uc = []
mc = []


def check_word_type(word):
    is_lower = True
    is_upper = True

    for char in word:
        if 'a' <= char <= 'z':
            is_upper = False
        elif 'A' <= char <= 'Z':
            is_lower = False
        else:
            is_lower = False
            is_upper = False
            break

    if is_lower:
        return 'lower'
    elif is_upper:
        return 'upper'
    else:
        return 'mixed'


for x in filter(None, re.split(separators, input())):
    word_type = check_word_type(x)
    if word_type == 'lower':
        lc.append(x)
    elif word_type == 'upper':
        uc.append(x)
    else:
        mc.append(x)

print('Lower-case:', ', '.join(lc))
print('Mixed-case:', ', '.join(mc))
print('Upper-case:', ', '.join(uc))

'''
Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.
'''
