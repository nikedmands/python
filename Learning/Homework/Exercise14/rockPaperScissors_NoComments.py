import random
loses_to = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}
choices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}
ai_choices = ["Rock", "Paper", "Scissors"]
user_score = []
ai_score = []


def check(user_choice, ai_choice):
    if ai_choice == loses_to[user_choice]:
        print("You win that round.")
        return user_score.append(1)
    elif user_choice == loses_to[ai_choice]:
        print("You lose that round.")
        return ai_score.append(1)
    else:
        print('Draw')


print("---------- WELCOME ----------")
name = input("What's your name: ").capitalize()
print('')
print("Welcome", name, "to Rock, Paper, Scissors.")
print("I'm sure you know the rules, so let's get started.")
print("First to 5 points wins!")
print('')


while len(user_score) < 5 and len(ai_score) < 5:
    user_guess = input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ").lower()
    if user_guess not in choices.keys():
        print("Please enter a valid response.")
        print('')
        continue
    user_guess1 = choices.get(user_guess)
    print('You chose: ', user_guess1)
    x = random.randint(0, 2)
    ai_guess = ai_choices[x]
    print('Comp chose: ', ai_choices[x])
    check(user_guess1, ai_choices[x])
    print('')

print("---------- Game Over -----------")
print(name, 'scored: ', len(user_score))
print('AI scored: ', len(ai_score))
if user_score > ai_score:
    print('YOU WON!')
else:
    print('LOL, you lost :(.')
print("Thanks for playing!")
