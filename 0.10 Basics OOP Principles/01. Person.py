class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter
    def name(self, _name):
        self._name = _name

    @property
    def age(self):
        return self._age

    @age.setter  # setter за age
    def age(self, _age):
        self._age = _age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


name = input()
age = int(input())
if len(name) < 3:
    print('Name\'s length should not be less than 3 symbols!')
elif age <= 0:
    print('Age must be positive!')
elif age > 15:
    print('Child\'s age must be less than 15!')
else:
    person = Person(name, age)
    print(person)


'''
Muncho
10
'''