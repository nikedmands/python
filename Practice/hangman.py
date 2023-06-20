import random
# create list
words_list = ['apple', 'banana', 'orange', 'pear', 'grape', 'kiwi', 'strawberry', 'blueberry', 'raspberry', 'mango', 'pineapple']


#  random choice from the list
random_choice = random.choice(words_list)
# character length of the word
length_of_choice = len(random_choice)

print('Welcome to hangman!')
print('Your hidden fruit to guess is', length_of_choice, 'letters long!')
print("~~~~~~~~~~~~~~~~~~", random_choice, "~~~~~~~~~~~~~~~~~~~~~~~~~~")

y = 1
while y == 1:
    letter = input('Please enter a letter: ')
    if letter in random_choice:
        print('Your letter was found')
        position = random_choice.index(letter)
        print(position)



    # user guess must be 1 letter
# user guess, if that character is in the new variable, show yes and its location
# loop guesses until correct word
# end if max guesses of 10 is reached

# start again? start ()