class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 100

    def UpdateName(self, newname):
        self.name = newname


    def UpdateBalance(self, bal):
        self.balance = bal

    def getInformation(self):
        print("name is " + self.name)
        print("age is " + str(self.age))

