def check_age(a):
    try:
        if int(a) > 0:
            print(name.capitalize() + " is " + age + " year(s) old")
    except ValueError:
        print("USE A NUMBER!")


name = input("Enter your name: ")
age = input("Enter your age: ")
result = check_age(age)
print(result)
