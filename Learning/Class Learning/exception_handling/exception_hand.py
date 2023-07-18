# file handling is just a way to type our own error messages, for security reasons
"""
try - test some blocks of code
except - handler errors when found in the block
else - execute code when there is no error
finally - execute code whether an error occurs or not
"""


def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed")
        return None
    except TypeError:
        print("Error: One of the values has a wrong type")
        return None
    except Exception as e:
        print("An unexpected error occurred with details: " + str(e))
        return None
    finally:
        print("Finally, the block ran")


# change these values to different datatypes, to get different error messages
firstNum = 5
secondNum = 2

result = divide(firstNum, secondNum)
print("Result is: " + str(result))
print('')


def deev(c, d):
    if d == 0:
        raise ValueError("Error occurred: Division by Zero")
    try:
        res = c / d
        return res
    except Exception as e:
        print("An error has occurred " + str(e))
        return None


res = deev(5, "0")
print("Result is: " + str(res))