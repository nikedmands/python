# open and append file called pelican.txt
run = open("pelican.txt", 'a')

# append the line of code in
file = open("pelican.txt", 'w')
file.write("A wonderful bird is the pelican,\n")

# append another line
file.writelines("His bill holds more than his belican.\n")

# create list
lines = ["He can take in his beak,\n", "Enough food for a week,\n",
         "But I'm dammed if I see how the helican.\n"]

# append the list to the file
file.writelines(lines)
# \n (line terminator) is required to move the following text to the next line

# run the script