# this 'hash bang' shows where python.exe is stored
#!/usr/bin/python

# Example Python script

# import the sys MODULE to use its functionality
import sys

# assign the argument_count VARIABLE the result from the len FUNCTION
# argv is part of the sys MODULE
# argv stands for ARGUMENT VECTOR a.k.a the list of parameters or inputs to the program
# argc is our variables the store the number of inputs to the program
argc = len(sys.argv)

# if (CONDITIONAL OPERATOR) the VARIABLE is greater than 1, then print 'Too many args'
if argc > 1:
    print('Too many args')
# otherwise, do this (i.e. print 'Hello...'
else:
    # give the VARIABLE where and string of text saying 'World'
    where = 'World'
    # basically print 'Hello World'
    print("Hello", where)

# print Goodbye from... and then CONCATENATE with the file directory location
# argv[0] is this script (this file) we are passing through the command (python.exe)
print('Goodbye from ' + sys.argv[0])

# if we add more arguments to the terminal, then this would return us with 'Too many args'
