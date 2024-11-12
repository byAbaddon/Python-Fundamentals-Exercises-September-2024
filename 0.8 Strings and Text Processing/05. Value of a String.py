txt, case = input(), input()
res = 0

for char in txt:
    if char.isalpha():
        if case == 'LOWERCASE' and char.islower():
            res += ord(char)
        if case == 'UPPERCASE' and char.isupper():
            res += ord(char)

print('The total sum is:', res)


'''
HelloFromMyAwesomePROGRAM
LOWERCASE
'''