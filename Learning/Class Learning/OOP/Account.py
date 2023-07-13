# a class is anything you want to storedata about. i.e. Person (name, age, height etc)
# public class variables are like a parent
# private class variables are only accessible to the class

# methods/procedures are like functions
# 'VERBS' methods for a class
# move/stop/change oil

# methods for person class can be 'run', 'jump'

class Account:
    # public class variable
    numCreated = 0
    # init is the constructor, init - create, self - new objects

    def __init__(self, initial):
        self.balance = initial
        # private class variable
        Account.numCreated += 1

    def deposit(self, amt):
        self.balance += amt
        return

    def withdraw(self, amt):
        self.balance -= amt
        return

    def getbalance(self):
        return self.balance


# OBJECTS, calling a class creates a new instance object
