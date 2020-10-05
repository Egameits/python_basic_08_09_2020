class Animal:
    name = 'SOME NAME'
    age = 0
    mass = 1

    def __init__(self, name, mass):
        print(id(self))
        self.name = name
        self.mass = mass


animal1 = Animal('Пес', 27)
print(id(animal1))
print('################' * 20)
animal2 = Animal('Кот', 8)
print(id(animal2))
