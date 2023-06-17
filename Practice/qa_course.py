# BOOLEAN
# Boolean True (always capitalized) is stored with a value of 1
print(True + True)
# =2
# Boolean False (always capitalized) is stored with a value of 0
print(True + False)
# =1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# NUMBERS
# Integers (whole number)
# Floating decimal points ('Floats' - decimal numbers)
# Equations always follow BODMAS (Brackets, Orders, Division, Multiplications, Addition, Subtractions)
a = 5 - 2 * 2
print(a)
# = 1, because 2 * 2 = 4, THEN 5 - 4 = 1
# Brackets come first though, with BODMAS
b = (5 - 2) * 2
print(b)
# = 6, because 5 - 2 = 3, THEN 3 * 2 = 6
# Division can return either an Integer OR Float
c = 17 / 3
d = 17 // 3
print(c)
print(d)
# c = 5.6666 (float), d = 5 (integer)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# STRINGS
# written in quotations
e = "Hello"
f = "World"
# CONCATENATION with the + symbol
# doesn't add any spacing
print(e + f)
# adds spacing
# multi-line strings need triple "
print(e, f)
g = """Hello
World"""
print(g)
# slicing a string. Counting from left starts at 0, counting from right starts at -1
a = "Hello World"
print(a)
b = a[1:5]
print(b)
# this shows 'ello'
# then with no end argument
b = a[2:]
print(b)
# this shows 'llo World'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# LISTS, SETS, DICTIONARIES
# Lists are generally used to similar data types, although not exclusively
a = [1, "string", True, 2.3]
print(a)
# slicing a list
# both of these will return the same answer
# start point is index 1, until the end
b = a[1:]
# start point is -3, until the end
c = a[-3:]
print(b)
print(c)
# adding to the end list
a.append("test")
print(a)
# inserting to a specific index, in this case to index position 2
a.insert(2, "myNewInsert")
print(a)
# print the number of index's in list a
print(len(a))
# replace a value in the list, replace starting at index position 1, and ending a index position 2
# this will replace string, with replace and 3
a[1:2] = ["replace", 3]
print(a)
# deleting index's
# delete the items starting at index 1, and ending, but not including, index 2. So just index 1
a[1:2] = []
print(a)
# or use the inbuilt del function. delete index 1, from list a
del (a[1])
print(a)
# put lists within other lists
c = [a, b]
print(c)
# you can append a list with itself...
c.append(c)
print(c)
# [...] refers to itself in the list
# list can contain multiple identical values
b.append(1)
b.append(1)
b.append(1)
b.append(1)
b.append(1)
print(b)
# SETS cannot contain identical values! and are immutable! (cannot be changed)
b = {1, "string", 2.3, 1, 1, True}
# sets items are unique, order in which it is printed is random.
# will remove boolean True also, as this is understood as a 1 under the hood.
print(b)
# sets would be good to store things like city names
# find if an item is within the list
if "string" in b:
    print(True)
# DICTIONARIES have key value pairs
a = {}
# looks like a set, but key value pairs are denotes with :
b = {'a': 1, 'b': 2, 'c': 3}
# in dictionary b, print 'a's key value pair
print(b['a'])
# change the key value pair
b['a'] = 'anything'
print(b)
# add a new key value pair
b[15] = 5
print(b)
# call list, to show just the keys within the dictionary
print(list(b))
# delete key value pairs
del (b[15])
print(b)
# test if something is in the dictionary
print('c' in b)
print('d' in b)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TUPLES
# ordered collection of values. are IMMUTABLE - cannot be changed
t = 1, 2, 3, 4
print(t)
print(t[0])
# new tuple, can include previous tuple
u = 7, t
print(u)
# get the length of a tuple. i.e. how many items are in the tuple
print(len(t))
t3 = 'hello',
# with a comma at the end, python now takes t3 as a tuple and NOT a string
print(len(t3))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# FUNCTIONS
# keyword "def" defines a function, : ends the concrete implementation.
def hello_world(s):
    return "Hello" + s


print(hello_world("world"))


def add(x, y):
    return x + y, x - y


# prints (8, 2). showing the 2 numbers added together, and the 2 numbers subtracted
print(add(5, 3))
# these outputs can be stored as a tuple
add_result, subtract_result = add(5, 3)
print(add_result)
print(subtract_result)


def reassign(number01):
    number01 = 2


number02 = 1
reassign(number02)
print(number02)


def reassign(number01):
    number01 = 2
    print(number01)


reassign(number02)
print(number02)


def reassign(list01):
    list01 = [2, 3]


def append(list02):
    list02.append(4)


# list 1, starts with list values
list03 = [0, 1]
reassign(list03)
# reassign does nothing because list01 has its own metadata
append(list03)
# append DOES change list03, because list02 and 03 have THE SAME metadata when list02 is initialized
print("List 03 =", list03)

