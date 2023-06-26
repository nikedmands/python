import time

# greeting message
print('Welcome to the typing test.')
print('')
print("Type the alphabet, in order. Don't forget to hit enter when you are finished!")
# get user ready to start the test with a simple user input
ready = input("Ready? (press 'y', then enter to begin. The timer will start as soon as you hit the enter key!): ")
# start the timer
timeA = time.time()
# user types
user_input = input('GO: ')
# count how long it took
timeB = time.time()
# variable to check user input against
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# if user input doesn't match the alphabet variable, print fail
if user_input != alphabet:
    print('You entered the alphabet incorrectly, feel free to try again.')
# else, if it was correct, show time taken
else:
    timeTaken = timeB - timeA
    # round the timeTaken variable to 2 decimal places
    timeTaken1 = float(round(timeTaken, 2))
    print('CORRECT, you took', timeTaken1, 'seconds.')
