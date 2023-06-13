print('Hello, welcome to Diagon Coffee!')

name = input('Can I take your name? ')

if name == 'Voldermort':
    evil_status = input('Are you actually Voldermort? ')
    if evil_status == 'Yes':
        print('You are not welcome here!')
        exit()
    else:
        print('Thank Dumbledore, I was worried then! Welcome')
else:
    print('Hello ' + name + ', thanks for coming in!' )

menu = 'Cappuccino, Latte, Espresso, Flat White, Macciato, Iced Vanilla Latte'

print(name + ', what can I get you today? here is our menu:\n' + menu)

order = input()

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

total_price = int(quantity) * price
print('Thank you, your order come to a total of: £' + str(total_price))

print('Perfect! We will have your ' + quantity + ' ' + order + 's ready for you in a moment, ' + name)