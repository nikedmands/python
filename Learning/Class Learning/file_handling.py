import os

# open in read mode
infile = open('file.txt', 'r')

# this will read the entire file
print(infile.read())
# close the file object, so it can be re-opened
infile.close()
print('')

# readlines
infile = open('file.txt', 'r')
line = infile.readlines()
print(line)
infile.close()
print('')

# read the whole file
lines = open('file.txt').read()
print(lines)
infile.close()
print('')

# splitlines
lines = open('file.txt').read().splitlines()
print(lines)
print('')


# safer recommended way to open files. WITH keyword will automatically close the file after
# you can see we call the file twice! once in the with loop, and then again after the line break
# we don't need to close the file again after when we use WITH
with open('file.txt', 'r') as infile:
    for line in infile:
        print(line, end='')

print('')

infile = open('file.txt').read()
print(infile)
print('')

# writing to files - this will REPLACE existing, with this new stuff
output = open('file.txt', 'w')
output.write("7\n")
output.close()


# append to a file, this will ADD new stuff to existing
output2 = open('file.txt', 'a')
output2.write('7\n')
output2.close()

# add a list to a file, without line terminator
fruits = ['oranges', 'mangoes\n']
output2.writelines(fruits)
output2.close()

# add a list to a file, with line terminator
fruits = ['oranges\n', 'mangoes\n']
output2.writelines(fruits)
output2.close()
# loop through each list item and add it into the file with for loop
# for fruit in fruits:
#     output2.write(fruit)
#     output2.write("\n")

# varFruit = 'banana'

output2.write("pineapple,banana")
output2.close()

# os.remove("file.txt")