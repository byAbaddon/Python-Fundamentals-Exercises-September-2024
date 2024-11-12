import re
import sys

input_text = sys.stdin.read()
pattern = r"<p>(.*?)<\/p>"

matches = re.finditer(pattern, input_text)

for match in matches:
    current_string = match.group(1)
    current_string = re.sub(r"[^a-z0-9]", " ", current_string)
    current_string = re.sub(r"\s+", " ", current_string)

    for char in current_string:
        if char.isalpha():
            if ord(char) <= ord('m'):
                new_char = chr(ord(char) + 13)
            else:
                new_char = chr(ord(char) - 13)
            print(new_char, end="")
        else:
            print(char, end="")

print()

