# import the random library
import random

# variable to keep count of the amount of lottery numbers randomly picked
lotto_count = 0
# a list of the stored lotto numbers
lotto_numbers = []

# welcome message
print('Welcome to the lottery generator!')
print('Here are your 6 random numbers between 1 and 50:')

# start of while loop, to continually run, until the condition is met (lotto_count variable is less than 6)
while lotto_count < 6:
    # variable number is assigned a value, randomly between 1 and 50
    number = random.randint(1, 50)
    # if the number has already been picked and is in the list, restart the loop by executing continue
    if number in lotto_numbers:
        continue
    # if number is not already in the list, then append the list by adding this number to the end
    else:
        lotto_numbers.append(number)
        # add 1 to the lotto_count variable to increase the count until it hits 6
        lotto_count += 1

# print the lotto_numbers list
print(lotto_numbers)
# goodbye message
print('Goodbye')