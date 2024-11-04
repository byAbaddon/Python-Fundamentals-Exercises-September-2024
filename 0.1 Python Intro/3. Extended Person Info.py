name = input()
age = int(input())
town = input()
salary = float(input())

print('Name:', name)
print('Age:', age)
print('Town:', town)
print('Salary:', f'${salary:.2f}')
print('Age range:', 'elder' if age >= 70 else 'adult' if age > 18 else 'teen')
print('Salary range:', 'high' if salary >= 2000 else 'medium' if salary > 500 else 'low')


'''
Gosho
20
Sofia
530
'''