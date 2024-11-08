from collections import Counter

obj = {float((k)): v for k, v in Counter(input().split()).items()}
sorted_obj = dict(sorted(obj.items(), key=lambda item: item[0]))
print('\n'.join(f"{k} -> {v} times" for k, v in sorted_obj.items()))


'''
8 2.5 2.5 8 2.5
'''
