import math

obj = {}

for city, n in [x.split() for x in iter(input, 'Aggregate')]:
    if city not in obj.keys():
        obj[city] = []
    if int(n) not in obj[city]:
        obj[city].append(int(n))

for k, v in obj.items():
    print(f'{k} -> {", ".join(map(str, v))} ({math.ceil(sum(v) - sum(v) / len(v))})')


'''
Sofia 2
Sofia 1
Plovdiv 100
Plovdiv 50
Aggregate
'''
