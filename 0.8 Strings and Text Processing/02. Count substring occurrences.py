import re

text = input().lower()
substr = input().lower()

matches = re.findall(f"(?={re.escape(substr)})", text)
print(len(matches))


'''
Welcome to the Software University (SoftUni)! Welcome to programming. Programming is wellness for developers, said Maxwell.
wel
'''