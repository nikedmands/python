import getpass

#variables
pin = 7412
attempts = 0
max_attempts = 3

print('Welcome to Nik banking, where we def WONT loose all your money!')

# start of while loop. WHILE condition is True, keep running.
while attempts < max_attempts:
    # users pic guess
    print('Please enter your 4 digit PIN.')
    print('You have', max_attempts - attempts, 'attempt(s) remaining!')
    guess = getpass.getpass(prompt="PIN:")
    # convert the guess to a number (input gives us a string)
    if len(guess) != 4:
        print('Incorrect amount of digits! Please enter your 4 digit PIN!')
        print('')
    else:
        guess = int(guess)
        # if the guess is identical to the pin, print 'Correct' & exit
        if guess == pin:
            print('Correct, you have 500 billion quid!')
            exit()
        # else, print line & +1 to attempts
        else:
            print('Wrong, please try again.')
            attempts += 1
            print('')

# if max number of attempts reached
# will only show when while condition is no longer attempts < max_attempts
print('Max number of attempts reach, account terminated!')

