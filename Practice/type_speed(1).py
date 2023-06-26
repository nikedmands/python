import time

# welcome message
print('Welcome to the typing test.')
print('')
print("Type the alphabet, in order. Don't forget to hit enter when you are finished!")
# take users name
ready = input("Ready? Enter your name, the timer will start as soon as you hit the enter key: ").capitalize()
# start an infinite loop
while True:
    # start the timer
    timeA = time.time()
    # type the alphabet
    user_input = input('GO: ')
    # stop the timer
    timeB = time.time()
    # variable to cross reference
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # if user input DOES NOT EQUAL variable
    if user_input != alphabet:
        response = input("Would you like to play again? ('y' for yes, 'n' for no): ").lower()
        # play again?
        if response == 'n':
            break
        elif response == 'y':
            continue
    else:
        # calculate time
        timeTaken = timeB - timeA
        # round to nearest 2 decimal places
        timeTaken1 = float(round(timeTaken, 2))
        print('CORRECT! Well done', ready, 'you took', timeTaken1, 'seconds.')
        response1 = input("Would you like to play again? ('y' for yes, 'n' for no): ").lower()
        # play again?
        if response1 == 'n':
            break
        elif response1 == 'y':
            continue

# print goodbye message
print('')
print('Thanks for playing', ready)
print('Goodbye!')