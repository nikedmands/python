# BASIC SINGLE AND MULTI LINE STRINGS

# string store a sequence of characters
someString = "Some String"

# multi line string
someString1 = """
some 
multi-line 
string
"""
print(someString)
print(someString1)
print('')
print('')

# STRING CHARACTER SEQUENCE POSITION
print(someString[0])
print(someString[1])
print('')
print('')

# STRING LENGTH
# could be good for checking if password entries are long enough
print(len(someString))
print('')
print('')

# LOOP OVER A STRING
# a for loop, just loops over a particular list or sequence of characters
# x is a variable, or an iterator
# it will continue to loop through the string until there are no more characters left
# I.E will print each character on a separate line
for x in someString:
    print(x)
print('')
# doesnt have to be a variable, can just be a string directly here
for x in "Sky":
    print(x)
print('')
print('')

# SOME STRING METHODS
# Conversion
number = 3
AString = '2'
# because one is a string and one is an integer, they CANNOT be added together
# would need:
print(number+int(AString))
print('')
print('')

# Upper and Lower case
print(someString.upper())
print(someString.lower())
print('')
print('')
# type full name separated by commas into a string variable and print the upper case and lower case instances
# of the string
# print out the length of your names combined
name = 'Nik, Edmands'
print(name.upper())
print(name.lower())
print(len(name))
print('')
print('')

# Replace
names = "John, Doe"
# replace returns a new copy of the variable, it DOES NOT change the original variable
print(names.replace("John", "Jane"))
print(names)
print('')
print('')

# Search a string
# print the index where it starts to find this in the string
print(names.find('Doe'))
# returns a boolean, True because it found this sequence, within the variable
print('Doe' in names)
# use this for a password to have particular set of characters, or not
print('x' in names)
print('')
print('')

# SLICING / SUBSTRING
# chose where to slice, using the start index, then the ending index (not inclusive of the ending index)
print(names[0:4])
print(names[:7])
print(names[-5:])
print('')
print('')

# STRIP - remove whitespaces. strip (leading and ending), rstrip (trailing) and lstrip (leading)
names2 = "      John, Doe      "
print(names2)
print("strip - remove trailing AND leading whitespace")
print(names2.strip())
print("rstrip - remove trailing whitespace")
print(names2.rstrip())
print("lstrip - remove leading whitespace")
print(names2.lstrip())
print('')
print('')

# CONCATENATE STRINGS
firstname = "John"
lastname = "Doe"
fullname = firstname + ' ' + lastname + ' ' + 'test'
print(fullname)

age = 20
# because we cant concatenate ints and strings, must convert the age to a str first
message = "I am " + str(age) + " years old"
print(message)
print('')
print('')

# FORMAT
# this way we don't have to convert the int, to a string. Format does this for us
# use curly brackets as placeholders for arguments
message1 = "I am {} years old"
print(message1.format(age))

message2 = "I am {} years old, and i like {}"
# formats can use variables or strings, each comma separates the placeholders
print(message2.format(age, "Python"))
print('')
print('')

# ENDSWITH & STARTSWITH
# can be a single character, or a sequence of characters, it's still a string!
message3 = "Welcome to Python"
# returns a boolean
print(message3.startswith("Welcome"))
print(message3.endswith("thon"))
# case sensitive!
print(message3.startswith("w"))
print(message3.endswith("L"))
print('')
print('')

# SPLIT A STRING INTO A LIST
message4 = "Welcome to Python's coolness"
# if no separator is defined, it uses a space as default
# could use a comma as the seperator: Splitlist = message4.split(',')
# prints the individual list items
print(message4.split())

# Iterate over the new list
Splitlist = message4.split()
# prints each iteration of the list
for x in Splitlist:
    print(x)
print('')
print('')

# ESCAPE CHARACTERS
# use backslash to allow illegal characters to still pass
message5 = "Hello world, it is \"sunny\" today"
print(message5)
# \n is the new-line character, just moves the text following it to the next line down
message6 = "Hello world, it is \nsunny today"
print(message6)
print('')
print('')

# EXERCISE 1 - count the number of vowels
sentence = input("Please enter your sentence: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
x = 0
for i in sentence:
    if i in vowels:
        x += 1
print("There are", str(x), "vowels in your sentence")

# EXERCISE 2 - reverse the string
ending = len(sentence)
print("Your sentence in reverse is:", sentence[ending::-1])

# EXERCISE 3 - counts words in the string, separated by spaces
count_words = sentence.split()
print("There is/are", len(count_words), "separate words in your sentence")
