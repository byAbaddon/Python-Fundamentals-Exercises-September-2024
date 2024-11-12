import re

data = input()
regex = r"\d{2}/[A-Z]{1}[a-z]{2}/\d{4}|\d{2}-[A-Z]{1}[a-z]{2}-\d{4}|\d{2}\.[A-Z]{1}[a-z]{2}\.\d{4}"
matches = re.findall(regex, data)
[print(f'Day: {d[0:2]}, Month: {d[3:6]}, Year: {d[-4:]}') for d in matches]


'''
13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
'''