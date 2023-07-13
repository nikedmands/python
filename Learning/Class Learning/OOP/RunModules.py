# OBJECTS, calling a class creates a new instance object
# from filename, import class
from Account import Account
from Person import Person
from Dog import Dog
from Dog import Bulldog

# instances of the account
# initialize the account with 1000
some_account = Account(1000.00)
# deposit 550.23
some_account.deposit(550.23)
# deposit some more
some_account.deposit(100)
# withdraw 50
some_account.withdraw(50)
# print the balance of the 'some_account@
print(some_account.getbalance())

# 'Nik' is a new instance of Account
Nik = Account(150)
Nik.withdraw(10)
print(Nik.getbalance())

# new instance created
Peter = Person("Peter", 21)
Peter.getInformation()
print("Peter's name is " + Peter.name)
print('')

# base/super class
mainDog = Dog("Justin")
print(mainDog.bark())

# derived class
bdog = Bulldog("Justin", "Bulldog")
# we have access to run as it is in the parent class
print(bdog.run())

