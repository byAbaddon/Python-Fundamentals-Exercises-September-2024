import re
from collections import defaultdict

pattern = r"([^&=?]*)=([^&=]*)"
regex = r"(%20|\+)+"

input_line = input()
while input_line != "END":
    pairs = re.findall(pattern, input_line)
    results = defaultdict(list)

    for field, value in pairs:
        field = re.sub(regex, " ", field).strip()
        value = re.sub(regex, " ", value).strip()
        results[field].append(value)

    print("".join(f"{key}=[{', '.join(values)}]" for key, values in results.items()))
    input_line = input()

