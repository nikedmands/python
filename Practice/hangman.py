import STUFF
# create list
list = ['apple', 'banana', 'orange', 'pear', 'grape', 'kiwi', 'strawberry', 'blueberry', 'raspberry', 'mango', 'pineapple']
user_list = []
#  random choice from the list
random_choice = random.choice(list)
# character length of the word
length_of_choice = len(random_choice)

print('Welcome to hangman!')
print('Your hidden fruit to guess is', length_of_choice, 'letters long!')

letter = input('Please enter one letter: ')
for c in range(0, length_of_choice):
    if random_choice[c] == letter:
        print(random_choice[c], end="")
    elif random_choice[c] == " ":
        print(" ", end="")
    else:
        print("-", end="")


# while True:
#     letter = input('Please enter one letter: ')
#     if len(letter) == 1:
#

# user guess must be 1 letter
# user guess, if that character is in the new variable, show yes and its location
# loop guesses until correct word
# end if max guesses of 10 is reached

# start again? start ()