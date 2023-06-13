# brand names and their sizes
NIKE = [6, 7, 8, 11, 12]
ADIDAS = [8, 12]
NEWBALANCE = [7, 8, 9, 10, 11]
HOKA = [11]

# dictionary of the brand names, and their store list of sizes
trainers = {"NIKE": NIKE,
            "ADIDAS": ADIDAS,
            "NEWBALANCE": NEWBALANCE,
            "HOKA": HOKA
            }

print('Welcome to our running trainer store!')
# input function, request an input from the user about how to proceed
request = input("Do you want to know about our trainer stock?")
# capitalize user input
request = request.capitalize()
# if statement to get a yes/no answer
if request != 'No':
    print("Cool, let's help you with that")
else:
    print('THEN WHAT ARE YOU DOING HERE?!?!')
    exit()

print('Our trainer brands available are Nike, Adidas, New Balance and Hoka.')
request = input('Which brand would you like to see the sizes we have availability for?')
# user input returned, turned into ALL capital letters, and spacing removed (if new balance is types)
request = request.upper().replace(" ", "")
# if user input is in trainer list, then find the sizes of that key ID and print them
if request in trainers:
    sizeList = trainers[request]
    print(sizeList)
else:
    print("Sorry, we don't stock that brand of trainer you have asked for, please try again.")
    exit()
