from re import findall

numbers = input()
regex = r'\b(?:0x)?[0-9A-F]+\b'
result = findall(regex, numbers)
print(*result)