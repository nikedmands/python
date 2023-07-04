class Dog:
    species = 'Cani'
    def __init__(self, name, age):
        self.name = name
        self.age = age


Buddy = Dog("Buddy", 9)

print(Buddy.name, Buddy.age)