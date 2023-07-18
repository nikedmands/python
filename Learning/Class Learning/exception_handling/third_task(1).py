def CheckNameAge():
    try:
        # take user inputs
        age = int(input("Enter your age: "))
        name = input("Enter your name: ")
        # if statement to check the age is valid (more than 0)
        if age < 0:
            # value error message, this shows if the number is less than 0
            raise ValueError("Error! Age must be greater than 0!")
        # print the outcome
        print(name.capitalize() + " is " + str(age))
    # wrong characters exception
    except Exception as t:
        print("Error! Enter the correct characters for age and name!" + str(t))


# call the function
try:
    # call the CheckNameAge function
    CheckNameAge()
except ValueError as e:
    print("Error " + str(e))

