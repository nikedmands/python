# string with items/elements
someString = 'Norwegian Blue', "Mr Khan's bike"

print("------------------- LIST -------------------")
# LIST - collection with items/elements
fruitList = ['banana', 'apples', 'guava', 'oranges']
numberList = [1, 3, 5, 7, 9]
print(fruitList)
print(numberList)

# Arithmatic operations on LIST
print("--- Arithmatic operations on a list")
print('min:', min(numberList))
print('max:', max(numberList))
print('sum:', sum(numberList))

# Access individual items using their index
print("--- Access individual items using their index")
print(numberList[0])
print(numberList[2])

# Length of a list
print("--- Length of a list")
print("Length of the list is:", len(numberList))

# Return a range of items from a list, start index(included): end index (excluded)
print("--- Return a range of items from the list")
print(numberList[1:3])

# Items from the beginning of list to a position
print("--- Items from beginning to a position")
print(numberList[:3])
print(numberList[3:])

# Change items
print("--- Change items")
numberList[0] = 20
numberList[3:] = [50, 50]
print(numberList)

# Add item to the list
print("--- Add item to the list")
fruitList += ['mangoes', 'pineapple']
print(fruitList)

# remove items
print("--- Remove items from a list")
fruitList.remove('mangoes')
print(fruitList)

# iterate or loop over a list
print("--- Iterate over a list")
for fruit in fruitList:
    print(fruit)

# occurrence of items in a list
print("--- Occurrence in a list")
count = fruitList.count('pineapple')
print("pineapples occur", count, "time(s)")

# find the index of an item
print("--- Find the index of an item")
fruitList.index('pineapple')
print(fruitList.index("pineapple"))

# sort list items
print("--- Sort list items")
fruitList.sort()
print(fruitList)
fruitList.sort(reverse=True)
print(fruitList)

print('')
print('')
print('')
print('')
print('')
print('')

# DICTIONARIES
print("------------------- DICTIONARIES -------------------")
mydict = {'Australia': 'Canberra', 'Eire': 'Dublin', 'France': 'Paris'}
print(mydict['Australia'])
country = 'Iceland'
mydict[country] = 'Reykjavik'
print(mydict)

# Dictionary storing an object of type list
print('--- Dictionary storing an object of type list')
mydict2 = {'UK': ['London', 'Wigan', 'Manchester'], 'US': ['Miami', 'New York', 'Boston']}
print(mydict2['UK'])

# add to dict
print('--- Add to dictionary')
mydict2['FR'] = ['Paris', 'Nice', 'Lyon']
print(mydict2['FR'][1])

# loop over a dictionary
print('--- Loop over items in dictionary')
for item in mydict2:
    print(mydict2[item])

# activity
# our attempt
print('--- Activity')
faveFruits = ['apple', 'banana', 'orange', 'strawberry']
# sort the list by length (key=len)
faveFruits.sort(key=len)
# print the last item in the list
print(faveFruits[-1])
# print the length of the last item in the list
print(len(faveFruits[-1]))

# peter
fruits = ["apple", "banana",  "watermelon", "pineapple"]
longest_fruit = ""
max_characters = 0
for fruit in fruits:
    if len(fruit) > max_characters:
        longest_fruit = fruit
        max_characters = len(fruit)
print("Fruit with the longest name:", longest_fruit)
print("Number of characters:", max_characters)

# jordan
fruits_List = ['Strawberries', 'Apples', 'Melon', 'Oranges']
print(fruits_List)
longest_fruit = max(fruits_List)
print('The longest fruit is', longest_fruit, '.')
print('It has ', len(longest_fruit), 'characters .')