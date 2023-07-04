# a) create a new file - could skip this step and go straight to append (this would create the file too)
file = open('country.txt', 'x')
file.close()

# b) append the file, to show a country on each line, with its length stated too
# append = is the call to open the file in append mode
append = open('country.txt', 'a')
# this is my list of countries
countries = ["England: 7\n", "France: 6\n", "Spain: 5\n", "USA: 3\n" "Australia: 9\n"]
# in the call, 'writelines' of countries list
append.writelines(countries)
# close the call
append.close()

# c) read back as dictionary data structure
# create empty dictionary
country_dict = {}
# pull_dict will be the call, to read mode the file
pull_dict = open("country.txt", "r")
# start to a loop, to extract the data into the empty dictionary
for line in pull_dict:
    # split at :
    x = line.split(": ")
    # country KEY is stored at index 0
    country = x[0]
    # length of the country is stored at index 1, but remove the \n printed at the end of the value
    length = x[1]
    # write the data to the dictionary, then move onto the next line
    country_dict[country] = length
pull_dict.close()
# show that the dictionary now contains values
print(country_dict)

# d) add another country to the dictionary
country_dict["Mexico"] = "6"
# show in the console that Mexico has been added
print(country_dict)

# e) iterate over the dictionary and append the file in format specified above
# iterate through the file using WITH
with open("country.txt", 'a') as f:
    # for loop to go through each item in the dictionary we appended in previous step
    for key, value in country_dict.items():
        # write the output in the form of a string for each key, value pair
        f.write('%s: %s\n' % (key, value))

# because we used append, this data has just been added below the previous data that we wrote to the file