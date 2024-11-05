n = abs(int(input()))
n_list = list(map(int, str(n)))

even_sum = 0
odd_sum = 0

for digit in n_list:
    if digit & 1:
        even_sum += digit
    else:
        odd_sum += digit

print(even_sum * odd_sum)


'''
12345
'''