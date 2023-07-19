# from classes.py, import all classes
from classes import *

# the classes present are:
# Person (parent class/superclass)
# Employee, Customer (both child classes/subclass


Steve = Person("Steve", 82, "Male")
print(Steve)
Nik = Employee("Nik", 32, "Male", "FS4116", "SE", "20,000")
print(Nik)
JohnSmith = Customer("John Smith", 22, "Female", 392870238)
print(JohnSmith)
Steve.change_name("James")
print(Steve)
Nik.change_gender("Female")
print(Nik)
Nik.update_salary("60,000")
print(Nik)
