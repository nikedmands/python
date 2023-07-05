# define a function


def first_function():
    print('My very first python function')


# call the function
first_function()


# parsing arguments into the function
def second_function(first_name):
    print('My name is ' + first_name)


second_function('Nik')
second_function('James')
# give an error, because the argument isn't supplied
# second_function()


def third_function(first_name, lastname):
    print('My name is ' + first_name + ' ' + lastname)


third_function('Nik', 'Edmands')

# error occurs because not all arguments have been supplied
# third_function('John')


# unspecified number of parameters
def forth_function(*params):
    print('the number of arguments is ' + str(len(params)) + ' the first item in our list is ' + params[0])


forth_function('test')
forth_function('test2', 'test')


def fifth_function(first_name, last_name):
    print('My full name is ' + first_name + ' ' + last_name)


fifth_function(first_name='John', last_name='James')


# multiple arguments with unspecified parameter names
def sixth_function(**params):
    print("the first argument is " + params['name'])


sixth_function(name='John')


def sixth_function(**params):
    print("the first argument is " + params['fname'] + ' and the second is ' + params["lname"])


sixth_function(fname='John', lname='James')


def seventh_function(age=25):
    print('My age is ' + str(age))


seventh_function(30)
seventh_function()

# functions accepting a list as an argument
ListOfCountries = ['UK', 'Germany', 'France', 'Spain']


def countries_func(countries):
    print('There are ' + str(len(countries)) + ' countries, and their names are;')
    for x in countries:
        print(x)


countries_func(ListOfCountries)

# functions using return keyword
# returns the value to the 'caller'


def number(num):
    return num


print(number(5))
AnotherNumber = number(5)
print(AnotherNumber)


# functions with an empty block of code. Use pass keyword to avoid compiler errors
def some_function():
    pass


# python recursion - a function calling itself
# factorial of a number


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


number = 6
print("The factorial of", str(number), "is:", str(factorial(number)))
print('')
print('')

# variable visibility in functions
result = 3


def scope_test1():
    result = 42


scope_test1()
print(result)


def scope_test2():
    global result
    result = 42

scope_test2()
print(result)