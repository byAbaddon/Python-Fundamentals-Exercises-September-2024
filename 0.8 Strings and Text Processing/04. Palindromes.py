txt = input().split()
result = [t for t in txt if t == ''.join(list(reversed(t)))]
unique_result = sorted(set(result), key=result.index)
# noinspection PyTypeChecker
print(', '.join(sorted(unique_result, key=str.lower)))


'''
Hi exe ABBA Hog fully a string ExE Bob
'''