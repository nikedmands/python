class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def uplift(self, uplift):
        self.salary = self.salary + uplift

    def showSalary(self):
        print(self.salary)

    def salaryDeduction(self, deduction):
        self.salary = self.salary - deduction

    def getInfo(self):
        print("The employees name is: " + self.name)
        print(self.name + "'s salary is: £" + str(self.salary))
        print("Their job title is: " + self.role)
        print('')

    def updateSalary(self, updatedSalary):
        self.salary = updatedSalary

