a = 5
b = 3

# IF
# must return a boolean value (True/False)
# not true so not statement at all
if a == b:
    print('a is equal to b')

print('')
print('')

# logical operators:
# not equal to !=

# find a string in list
lang = ['Perl', 'Python', 'PHP', 'Ruby']
if 'Python' in lang:
    print('Python is found')

# ELIF (else if)
# do the checks in order from top to bottom, whenever it is correct, print that line
if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('some other expected condition')

# chained conditionals
number = 5
distance = 42
if 0 < number < 42 < distance:
    print('num and dist are within range')
# prints nothing until the else statement is stated, as above statement is false
else:
    print('num and dist are out of range')

# logical AND operator
if 0 < number and number < 42 and 42 < distance:
    print('num and dist are within range')
else:
    print('hello')

myList = [1, 2, 3, 5, 7, 9]
# this returns a True boolean, I.E the number is 1 (boolean - True - 1)
if myList:
    print('The list is not empty')

myList2 = [0, 1, 2, 3]
# this returns a False boolean, I.E the number 0 (boolean - False - 0)
# IF NOT ALL - returns false because not ALL the items in the list are 0's
if not all(myList2):
    print('not all are true')

myList3 = [0, 1, 2, 3]
# ANY - returns false because not ALL the items in the list are 0's
if any(myList3):
    print('at least one item is true')

# Object types
num = 42
txt = '3'

# this will give an error, as txt is a string, num is an integer
# if txt < num:
#     print('txt is less than num')

# change the string value txt, into a number (integer)
if int(txt) < num:
    print('txt is less than num')

# WHILE
# will keep looking until the condition has been met
# line currently = None (in python this = NOTHING, I.E EMPTY)
# line will then become the users typed word
# while line DOESNT = 'done', the loop will keep running
line = None
while line != 'done':
    line = input('type "done" to complete: ')
    print('<', line, '>')

# need an exit condition, else the loop will run forever (endless loop)
i = 1
while i < 6:
    print(i)
    i += 1

# IF statement, within the WHILE LOOP
l = 1
while l < 6:
    print(l)
    if l == 4:
        print('The value of l is 4')
    l += 1

# BREAK statement
r = 1
while r < 8:
    print(r)
    if r == 4:
        break
    r += 1

# CONTINUE statement, this one will skip the number 4, as when d == 4 we must CONTINUE the while loop
d = 1
while d < 8:
    d += 1
    if d == 4:
        continue
    print(d)

# WHILE WITH ELSE
# this will then do something else, once the True part of the loop is now False
# basically now the condition is False
w = 1
while w < 8:
    w += 1
    print(w)
else:
    print('w is no longer less than 8')

# FOR LOOPS
# iterate through a sequence, often a list or tuple
# 'for' 'variable' 'in' 'object':
# loop body
# for loop
fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    # just prints each index in the fruits list
    print(x)

# FOR LOOP WITH BREAK
# this list won't show grape
fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)
    if x == 'orange':
        break

# task:
fave_letters = ['e', 'r', 'o', 'm', 'n']
print('This is a list of my favourite letters:')
for x in fave_letters:
    print(x)

print('')
print('')

fave_foods = ['sweets', 'enchiladas', 'pasta', 'zebra', 'chocolate']
for x in fave_foods:
    print(x)
    # this will break the FOR LOOP, then the variable x starts with the letter p
    if x.startswith('p'):
        break

print('')
print('')

# will just print each index of the string
for x in 'banana':
    print(x)

print('')
print('')

# FOR RANGE
some_list = ['John', 'Jack', 'Jim', 'Joe']
# len = number of items in some_list
for i in range(0, len(some_list)):
    # range will = 0 - 4
    # then print each index, one by one, so index 0, then index 1 etc... (and show the index number)
    print(some_list[i], i)

print('')
print('')

# for loops breaks once index 2 (Jim) is reached
for i in range(0, len(some_list)):
    if i == 2:
        break
    print(some_list[i], i)

print('')
print('')

# FOR RANGE WITH STEP
# start with 2, end at 20, in 2 step increments
# START, STOP, STEP
for x in range(2, 20, 2):
    print(x)
# else is used when the condition is False, i.e. when the loop is done
else:
    print('Finished!')

print('')
print('')

# same as above, but using variables for our start, stop and step
start = 1
stop = 21
step = 4
for x in range(start, stop, step):
    print(x)
else:
    print('Finished!')

