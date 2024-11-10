class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def produce_sound(self):
        pass


class Dog(Animals):
    def __init__(self, name, age, number_of_legs):
        super().__init__(name, age)
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."


class Cat(Animals):
    def __init__(self, name, age, intelligence_quotient):
        super().__init__(name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."


class Snake(Animals):
    def __init__(self, name, age, cruelty_coefficient ):
        super().__init__(name, age,)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."


dogs = {}
cats = {}
snakes = {}

while True:
    command = input()
    if command == "I'm your Huckleberry":
        break

    parts = command.split()
    if len(parts) == 4:
        animal_class, name_a, age_a, val = parts
        age_a = int(age_a)
        val = int(val)

        if animal_class == 'Dog':
            dogs[name_a] = Dog(name_a, age_a, val)
        elif animal_class == 'Cat':
            cats[name_a] = Cat(name_a, age_a, val)
        elif animal_class == 'Snake':
            snakes[name_a] = Snake(name_a, age_a, val)
    elif len(parts) == 2 and parts[0] == 'talk':
        name_a = parts[1]
        if name_a in dogs:
            print(dogs[name_a].produce_sound())
        elif name_a in cats:
            print(cats[name_a].produce_sound())
        elif name_a in snakes:
            print(snakes[name_a].produce_sound())

for name, dog in dogs.items():
    print(f"Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.number_of_legs}")

for name, cat in cats.items():
    print(f"Cat: {cat.name}, Age: {cat.age}, IQ: {cat.intelligence_quotient}")

for name, snake in snakes.items():
    print(f"Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.cruelty_coefficient}")


'''
Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry
'''