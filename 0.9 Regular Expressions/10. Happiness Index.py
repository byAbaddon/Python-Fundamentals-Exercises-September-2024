import re
# :TODO ---------------------
happy_emoticons = r":\)|:D|;\)|:\*|:\]|;\]|:\}|;\}|\(:|\*:\|c:|\[:|\[;"
sad_emoticons = r":\(|D:|;\(|:\[|;\[|:\{|;\{|\):|:c|\]:|];"

text = input()
happy_count = len(re.findall(happy_emoticons, text))
sad_count = len(re.findall(sad_emoticons, text))

if sad_count == 0:
    happiness_index = happy_count
else:
    happiness_index = round(happy_count / sad_count, 2)

if happiness_index >= 2:
    result = ":D"
elif happiness_index > 1:
    result = ":)"
elif happiness_index == 1:
    result = ":|"
else:
    result = ":("

print(f"Happiness index: {happiness_index:.2f} {result}")
print(f"[Happy count: {happy_count}, Sad count: {sad_count}]")


'''
&&:(&:)z:)zz%%!%%!%%!%:(
'''