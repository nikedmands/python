# open, read, slurp pelican file
f = open("pelican.txt", 'r')

peli = f.read()
print(type(peli))
# read the file and print the type of date to the console
print(type(f))
# print the file contents to the console
print(f.read())
f.close()

# '_io.TextIOWrapper' is the type of data

# read file into a list, then output the number of items in the list
with open("pelican.txt") as x:
    pelican_list = x.readlines()
print("The pelican file list is", len(pelican_list), "items long")
print('')

# use loop to iterate over and print contents of the file. Don't include blank lines
with open("pelican.txt") as x:
    # start for loop, looping each line in x
    for line in x:
        # print the line, strip will remove the \n new line terminator (remove the empty lines between)
        print(line.strip())

