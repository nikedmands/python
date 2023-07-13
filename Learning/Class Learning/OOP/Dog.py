class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("WOOF")

    def run(self):
        print(self.name + " is running")


# put parent class/superclass in brackets of this child class/subclass
class Bulldog(Dog):
    def __init__(self, name, breed):
        # need to send the bulldogs name to the parent function
        super().__init__(name)
        # self.breed = "Bulldog"
        self.breed = breed

    # this child method, will override the parent method, therefore, booyakasha will be called NOT woof
    def bark(self):
        print("BOOYAKASHA")

    def Stroke(self):
        print("stroking " + self.name)
