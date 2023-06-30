import random

# dictionary to store what loses as a key, value pair
loses_to = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}
# dictionary used to allow user to enter r, p, s
choices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

# separate list so the AI choice can be picked from a random int between 0-2
# 0 = rock, 1 = paper, 2 = scissors
ai_choices = ["Rock", "Paper", "Scissors"]

# use a length of a list to keep the score
user_score = []
ai_score = []


def check(user_choice, ai_choice):
    # IF to check the random AI choice has a value pair in the 1st dictionary
    if ai_choice == loses_to[user_choice]:
        # if the AI loses, the user wins
        print("You win that round.")
        # append the users score list with an item (1)
        return user_score.append(1)
    # ELIF to check the user choice has a value pair in the 1st dictionary
    elif user_choice == loses_to[ai_choice]:
        # if the user loses, the AI wins the round
        print("You lose that round.")
        # append the AI score list with an item (1)
        return ai_score.append(1)
    else:
        # if the 2 previous IF's failed, then it was a draw
        print('Draw')


# WELCOME
print("---------- WELCOME ----------")
name = input("What's your name: ").capitalize()
print('')
print("Welcome", name, "to Rock, Paper, Scissors.")
print("I'm sure you know the rules, so let's get started.")
print("First to 5 points wins!")
print('')

# start a while loop, will keep running WHILST either score is < 5 (score limit)
while len(user_score) < 5 and len(ai_score) < 5:
    # user guess is a single, lower case char
    user_guess = input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ").lower()
    # check if this char is NOT IN the choices dictionaries keys list, restart the while loop
    if user_guess not in choices.keys():
        print("Please enter a valid response.")
        print('')
        continue
    # get the value of the key entered by the user, from choice dictionary
    # this can then be used to check against key:values in the loses_to dictionary
    user_guess1 = choices.get(user_guess)
    # show users choice (picked as the value, against the key the user entered)
    print('You chose: ', user_guess1)
    # generate random in for AI random guess. this will give us the index to search the ai_choices list
    x = random.randint(0, 2)
    # assign variable with the random choice from the list
    ai_guess = ai_choices[x]
    # show the AI guess
    print('Comp chose: ', ai_choices[x])
    # run the 2 guesses through the function
    check(user_guess1, ai_choices[x])
    print('')

# ENDING
print("---------- Game Over -----------")
print(name, 'scored: ', len(user_score))
print('AI scored: ', len(ai_score))
if user_score > ai_score:
    print('YOU WON!')
else:
    print('LOL, you lost :(.')
print("Thanks for playing!")
