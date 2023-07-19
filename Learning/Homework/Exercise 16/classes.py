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


class Employee(Person):
    def __init__(self, name, age, gender, employee_id, job_role, salary):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.job_role = job_role
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Job Role: {self.job_role}, Salary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary


class Customer(Person):
    def __init__(self, name, age, gender, customer_num):
        super().__init__(name, age, gender)
        self.customer_num = customer_num

    def __str__(self):
        return f"{super().__str__()}, Customer Number: {self.customer_num}"
