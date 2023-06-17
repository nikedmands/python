# brand names and their sizes
NIKE = [6, 7, 8, 11, 12]
ADIDAS = [8, 12]
NEWBALANCE = [7, 8, 9, 10, 11]
HOKA = [11]

# dictionary of the brand names, and then store list of sizes
trainers = {"NIKE": NIKE,
            "ADIDAS": ADIDAS,
            "NEWBALANCE": NEWBALANCE,
            "HOKA": HOKA
            }

print('Welcome to our running trainer store!')
# input function, request an input from the user about how to proceed
request = input("Do you want to know about our trainer stock? ")
# capitalize user input
request = request.capitalize()
# if statement to get a yes/no answer
if request != 'No':
    print("Cool, let's help you with that")
else:
    print('THEN WHAT ARE YOU DOING HERE?!?!')
    exit()

print('We currently stock Nike, Adidas, New Balance and Hoka trainers.')
# while loop, takes argument, checks for validity, and doesn't continue until condition is met
while True:
    # user input question
    user_request = input('Which brand would you like to see the sizes we have availability for? ')
    # print line, with users input inside
    print("Ok, let's take a look for", user_request, "trainers in our lists..")
    # change the users input to one whole word (useful for new balance),
    # then all uppercase (to check against trainers list)
    request_caps = user_request.upper().replace(" ", "")

    # if not statement. example: if request_caps IS NOT in trainers
    if not request_caps in trainers:
        # print this, and return to the beginning of the while loop
        print("Sorry, but that didn't match in any of our lists. Please try again.")
    else:
        # now the condition has been met, exit the while loop
        break

# new variable which has user's requested trainer brands available sizes.
sizeList = trainers[request_caps]
print("Here are the sizes we have available:")
print(sizeList)



# if request_caps in trainers:
#     sizeList = trainers[request_caps]
#     print("Here are the sizes we have available:")
#     print(sizeList)
# else:
#     print("Sorry, we don't stock that brand of trainer you have asked for, please try again.")
#
# input("Is there anything else we can help with?")
