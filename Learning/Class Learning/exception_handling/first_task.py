def divide(a, b):
    try:
        result = int(a) / int(b)
        return result
    except ZeroDivisionError:
        print("DIVISION BY ZERO NOT ALLOWED!!!!!")
        return None
    except TypeError:
        print("USE NUMBERS")
        return None
    except ValueError:
        print("One of your inputs was not an INT")


a = input("First: ")
b = input("Second: ")
result = divide(a, b)
print(result)

