class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Gender: {self.gender})"

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def change_gender(self, new_gender):
        self.gender = new_gender


class Customer(Person):
    def __init__(self, name, age, gender, customer_num, balance):
        super().__init__(name, age, gender)
        self.customer_num = customer_num
        self.balance = balance

    def __str__(self):
        return f"{super().__str__()}, Customer Number: {self.customer_num}"

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self):
        amount = int(input("Please enter the amount you with to withdraw: "))
        try:
            if (self.balance - amount) > 0:
                self.balance = self.balance - amount
        except InsufficientFundsException as err:
            print("Error: Insufficient Funds")

    def get_info(self):
        return f"-----\n{super().__str__()} \nCustomer Number: {self.customer_num}\nBalance: {self.balance}\n-----\n"


class InsufficientFundsException:
    pass

