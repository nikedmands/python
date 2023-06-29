# create a new file
file = open('country.txt', 'x')
file.close()

# dictionary of countries
countries_dict = {'England': 7, 'Spain': 5, 'France': 6, 'Germany': 7, 'Sweden': 6}

# append dictionary to file
with open('country.txt', 'w') as f:
    print(countries_dict, file=f)


