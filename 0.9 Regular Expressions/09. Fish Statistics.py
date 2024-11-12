import re

input_string = input()
pattern = r"(>*)<(\(+?)(['\-x])>"
matches = re.finditer(pattern, input_string)
count = 1

if not any(matches):
    print("No fish found.")
else:
    for match in re.finditer(pattern, input_string):
        print(f"Fish {count}: {match.group(0)}")
        tail_count = len(match.group(1)) * 2

        if tail_count == 0:
            print("Tail type: None")
        elif len(match.group(1)) == 1:
            print(f"Tail type: Short ({tail_count} cm)")
        elif 1 < len(match.group(1)) <= 5:
            print(f"Tail type: Medium ({tail_count} cm)")
        else:
            print(f"Tail type: Long ({tail_count} cm)")

        body_length = len(match.group(2)) * 2

        if len(match.group(2)) <= 5:
            print(f"Body type: Short ({body_length} cm)")
        elif 5 < len(match.group(2)) <= 10:
            print(f"Body type: Medium ({body_length} cm)")
        else:
            print(f"Body type: Long ({body_length} cm)")

        status = match.group(3)
        if status == "'":
            print("Status: Awake")
        elif status == "-":
            print("Status: Asleep")
        elif status == "x":
            print("Status: Dead")

        count += 1
