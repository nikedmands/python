import random

# generate a random number, between 1-100
num = random.randint(1, 101)
# guesses variables
max_guess = 10
guess = 0

x = 'y'

while x == 'y':
    # welcome
    print('Welcome to the number guessing game. Please guess the number between 0 - 100')
    # start or while loop
    # run loop whilst number of users guess < 10
    while guess < max_guess:
        # users guess
        user_num = input('Please make a guess: ')
        # add 1 to users guesses variable
        guess += 1
        # turn the string from input, into an integer
        user_num = int(user_num)
        # if the guess is less than num, print too low
        if user_num < num:
            print('Your guess was too low, please try again.')
        # else if the guess is too high, print too high
        elif user_num > num:
            print('Your guess was too high, please try again.')
        # else, if none of the above have been met, the guess must == num
        else:
            print('CORRECT!')
            # print guess variable (counter)
            print('It only took you', guess, 'attempt(s)!')
            exit()
# this will print it the while loop didn't run (i.e. guess no longer less than 10, max number of guesses allowed)
print('Too many attempts. Goobye!')
exit()