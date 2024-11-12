from re import finditer

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
numbers = input()
results = finditer(pattern, numbers)
[print(result.group(0), end=' ') for result in results]


'''
1 -1 1s 123 s-s -12
'''