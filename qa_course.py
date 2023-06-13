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
print(e , f)
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
b = a[1:]
c = a[-3:]
print(b)
print(c)
# adding to the end list
a.append("test")
print(a)
# inserting to a specific index
a.insert(2, "myNewInsert")
print(a)
# print the number of index's in list a
print(len(a))

