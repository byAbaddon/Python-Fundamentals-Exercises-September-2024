words_dict = {}
for x in [x.lower() for x in input().split()]:
    if x not in words_dict.keys():
        words_dict[x] = 1
    else:
        words_dict[x] += 1

print(', '.join(k for k, v in words_dict.items() if v & 1))
'''
Java C# PHP PHP JAVA C java
'''