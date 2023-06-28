def add(num1, num2):
    answer = num1 + num2
    print(num1, '+', num2, '=', answer)


def sub(num1, num2):
    answer = num1 - num2
    print(num1, '-', num2, '=', answer)


def div(num1, num2):
    answer = num1 / num2
    print(num1, '/', num2, '=', answer)


def mul(num1, num2):
    answer = num1 * num2
    print(num1, '*', num2, '=', answer)


response_list = ['1', '2', '3', '4']
while True:
    print("""
Welcome to the calculator!
Enter 1 for addition.
Enter 2 for subtraction.
Enter 3 for division.
Enter 4 for multiplication.
Enter 'e' to exit.""")

    user_request = input('Which function would you like to use?: ')
    if user_request == 'e':
        print('Goodbye.')
        exit()
    elif user_request not in response_list:
        print('Please choose a valid response.')
        continue
    else:
        numberOne = input('Please enter your first number: ')
        numberOne = int(numberOne)
        numberTwo = input('Please enter your second number: ')
        numberTwo = int(numberTwo)

        if user_request == '1':
            add(numberOne, numberTwo)
        elif user_request == '2':
            sub(numberOne, numberTwo)
        elif user_request == '3':
            div(numberOne, numberTwo)
        elif user_request == '4':
            mul(numberOne, numberTwo)
        elif user_request == 'e':
            exit()
        else:
            print('Please enter a valid option.')

