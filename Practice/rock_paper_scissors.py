import random

# list of choices available
choices = ['rock', 'paper', 'scissors']
# track scores
comp_score = 0
user_score = 0

# opening print
print('Welcome to Rock, Paper, Scissors. First to 10 wins!')
# while true loop, keeps running until a condition is met
while True:
    # if score has been reached, break from the loop
    if user_score == 10 or comp_score == 10:
        break
    #users guess, or q for quit
    user_guess = input('Please enter either "rock", "paper" or "scissors", or "Q" to end the game: ').lower()
    # user wants to quit, so break the loop
    if user_guess == 'q':
        break
    # if invalid choice, restart the loop (continue)
    if user_guess not in choices:
        print("Please try again with one of the specified options.")
        print("")
        continue
    # create a random int between 0 and 2
    x = random.randint(0, 2)
    # find that index in the choices list, and select that as the computers choice
    comp_guess = choices[x]
    # print the computers choice
    print("The computer picked", comp_guess + ".")
    # rock beats scissors
    if user_guess == 'rock' and comp_guess == 'scissors':
        user_score += 1
        print('Well done, you won that round!')
        print("")
    # scissors beats paper
    elif user_guess == 'scissors' and comp_guess == 'paper':
        user_score += 1
        print('Well done, you won that round!')
        print("")
    # paper beats rock
    elif user_guess == 'paper' and comp_guess == 'rock':
        user_score += 1
        print('Well done, you won that round!')
        print("")
    # if the same guess, no score, restart the guess
    elif user_guess == comp_guess:
        print('Draw, go again!')
        print("")
    # all other possibilities would result in the computer wining the round
    else:
        comp_score += 1
        print('Woops, you lost that round!')
        print("")

print("")
print("")
print("Thanks for playing!")
print("Your score was:", user_score)
print("The computer's score was:", comp_score)
print("")
if user_score > comp_score:
    print("Well done! You WON!")
elif user_score == comp_score:
    print("It was a draw, better luck next time!")
else:
    print("Sorry, you lost. Better luck next time!")
print("")
print("")
exit()