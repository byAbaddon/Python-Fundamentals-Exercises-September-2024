def int_number(n):
    condition = 'negative' if n < 0 else 'positive' if n > 0 else 'zero'
    print('The number', n, 'is', condition + '.')


int_number(int(input()))

'''
int_number(2)
int_number(-5)
int_number(0)
'''