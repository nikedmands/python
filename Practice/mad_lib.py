list = []

# max length of list = 10
while len(list) < 10:
    change = input('Please enter a word to add to the list: ').capitalize()
    if change in list:
        print('Sorry, the list cannot take duplicate entries')
        continue
    list.append(change)

answer = input('Would you like to show your completed list? ').lower()
if answer == 'yes':
    print(list)
else:
    print('Goodbye!')
    exit()

answer1 = input('Would you like to change any of the values in the list? ').lower()
if answer1 == 'yes':
    change_value = input('Please type the name you wish to change: ').capitalize()
    if change_value in list:
        print('You would like to change', change_value)
        change_to = input('What would you like to change this to? ')
        index = list.index(change)
        print(index)
    else:
        print('Sorry, that name does not exist in the list.')