from banking_classes import *

Nik = Customer("Nik", 32, "Male", 3837, 2000)
print(Nik.get_info())
Nik.deposit(350)
print(Nik.get_info())
Nik.withdraw()
print(Nik.get_info())


