import random

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#%&()*+,-./:;<=>?@[\]^_`{|}~"

print('Welcome to the password generator.')
char_amount = input("How many characters do you want the password to be?: ")
char_amount = int(char_amount)
pass_amount = input("How many passwords would you like to generate?: ")
pass_amount = int(pass_amount)

for pwd in range(pass_amount):
    passwords = ''
    for c in range(char_amount):
        passwords += random.choice(characters)
    print(passwords)
