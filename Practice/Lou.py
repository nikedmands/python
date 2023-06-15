# this is an input function, the program will wait for the user to input their name and store that ready for later use
name = input('Can I take your name? ')

# adding if/else statements. in this example, Voldermort is nor welcome into the coffee shop
if name == 'Voldermort':
    evil_status = input('Are you actually Voldermort? ')
    if evil_status == 'Yes':
        print('You are not welcome here!')
        exit()
    else:
        print('Thank Dumbledore, I was worried then! Welcome')
else:
    print('Hello ' + name + ', thanks for coming in!' )

# using the concatenation method to complete the sentence with the users input
print('Hello ' + name + ', thanks for coming in!' )
# Example of a menu set in a dictionary class
menu = 'Cappuccino, Latte, Espresso, Flat White, Macciato, Iced Vanilla Latte'

# creating a menu for the customer to choose from
# this print function will have the string with the variable added of menu
print(name + ', what can I get you today? here is our menu:\n' + menu)
# this will allow the user to browse the menu and input their order
order = input()
# order received, now printing a string, input, string, input
price = 3.50
quantity = input('How many would you like? ')

if order == 'Cappuccino':
    price = 4
elif order == 'Latte':
    price = 4
elif order == 'Espresso':
    price = 2.50
elif order == 'Flat White':
    price = 3.50
elif order == 'Macciato':
    price = 4.50
elif order == 'Iced Vanilla Latte':
    price = 5

# converting the input into an integer for python to create the maths
total_price = int(quantity) * price
# converting the integer back to a string for the program to concatenate the sentence together
print('Thank you, your order come to a total of: £' + str(total_price))

print('Perfect! We will have your ' + quantity + ' ' + order + 's ready for you in a moment, ' + name)